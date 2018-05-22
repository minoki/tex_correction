#!/usr/bin/env python3

import sys, os

template_before = r"""\documentclass[dvipdfmx]{jsarticle}
\usepackage{correction}
\newtcblistingExpand{corlisting}{\tcboptions,minted options={\mintedoptions}}
\newcommand{\bs}{\symbol{"5C}}
\newcommand{\minus}{-}
\let\m\minus

\begin{document}

\begin{corlisting}
"""

template_after = r"""\end{corlisting}
\end{document}
"""

def create_from_texsrc(src):
    src_notab = src.replace("\t", "  ")
    return template_before + src_notab + template_after

if __name__ == '__main__':
    report_path = os.path.abspath(sys.argv[1])
    if not os.path.exists(report_path):
        print("File not found: " + report_path)
        sys.exit(1)
    report_basename = os.path.basename(report_path)
    root, ext = os.path.splitext(report_basename)
    if ext != ".tex":
        print("Not tex source: " + report_path)
        sys.exit(1)
    report_dir = os.path.dirname(report_path)
    os.chdir(report_dir)
    with open(report_basename, "r") as report_file:
        with open("correction_"+root+".tex", "w") as out_file:
            out_file.write(create_from_texsrc(report_file.read()))
