# TeX課題添削テンプレート

詳しくは [usage.pdf](usage.pdf) と [usage.tex](usage.tex) を参照。

## 準備

* Python/Pygmentsのインストール。`pip install pygments` 等。
* `correction.sty` を適切な場所に配置する。`kpsewhich -var-value=TEXMFHOME` の出力を参考にせよ。
    * 例：`~/texmf/tex/correction.sty`, `~/Library/texmf/tex/correction.sty`

## 使い方

* `/path/to/提出課題.tex` に対して `python3 create.py /path/to/提出課題.tex` とすると `/path/to/correction_提出課題.tex` が作られる。
* 添削する人は `/path/to/correction_提出課題.tex` を編集する。
* タイプセットは `platex -shell-escape correction_提出課題.tex` という感じ。正しい出力を得るには複数回タイプセットが必要になる。latexmkやcluttexを使うと良いだろう。
* コード中の添削したい部分には `@@` で囲ったTeXコードを書くが、受講生の提出したTeXソースの中にすでに `@` が登場していると都合が悪い。その場合は他の文字をエスケープ文字として使う。[usage.tex](usage.tex) の冒頭のコメントを参照。
