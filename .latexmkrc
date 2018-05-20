#!/usr/bin/env perl

$latex = 'platex -shell-escape -halt-on-error -synctex=1'; #-synctex=1
$latex_silent = 'platex -halt-on-error -synctex=1 -interaction=batchmode'; #-synctex=1
$bibtex = 'pbibtex';
$dvipdf = 'dvipdfmx %O -o %D %S';
$makeindex = 'mendex %O -o %D %S';
$max_repeat = 5;
$pdf_mode = 3; # generates pdf via dvipdfmx

# Prevent latexmk from removing PDF after typset.
# This enables Skim to chase the update in PDF automatically.
$pvc_view_file_via_temporary = 0;

$pdf_previewer = "evince";

# latexmk -C
$clean_ext = 'bbl synctex.gz';
