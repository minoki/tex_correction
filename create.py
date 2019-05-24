#!/usr/bin/env python3

import sys, os, codecs, chardet

template_before = r"""\documentclass[dvipdfmx]{jsarticle}
\usepackage{correction}
\newtcblistingExpand{corlisting}{\tcboptions,minted options={\mintedoptions}}

\begin{document}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{corlisting}
"""

template_after = r"""\end{corlisting}
\end{document}
"""

def create_from_texsrc(src):
    src_notab = src.replace("\t", "  ").replace("\r\n", "\n")
    return template_before + src_notab + template_after

def get_encoding(filepath):
    with open(filepath, mode="rb") as f:
        binary = f.read()
        return chardet.detect(binary)["encoding"]

if __name__ == '__main__':
    report_path = os.path.abspath(sys.argv[1])
    # ファイルの存在とか拡張子とかをチェック
    if not os.path.exists(report_path):
        print("File not found: " + report_path)
        sys.exit(1)
    report_basename = os.path.basename(report_path)
    root, ext = os.path.splitext(report_basename)
    if ext != ".tex":
        print("Not tex source: " + report_path)
        sys.exit(1)
    print("Creating from: " + report_path)
    # レポートのファイルがあるディレクトリで作業
    report_dir = os.path.dirname(report_path)
    os.chdir(report_dir)
    encoding = get_encoding(report_path)
    out_filename = "correction.tex"
    # 当初は "correction"+root+".tex"にしてたが，
    # 日本語を含むファイル名でplatexがエラーを吐いたので，こっちに修正
    if os.path.exists(out_filename):
        print("Already exists: " + out_filename)
        sys.exit(1)
    with codecs.open(report_basename, "r", encoding) as report_file:
        with open(out_filename, "w") as out_file:
            out_file.write(create_from_texsrc(report_file.read()))
