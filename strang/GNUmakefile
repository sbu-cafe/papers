EPStoPDF = epstopdf

ALL: paper.pdf 

eps_source = $(wildcard *.eps)
png_source = $(wildcard *.png)

tpdf_source = $(wildcard *.pdf)
pdf_source = $(filter-out paper.pdf, $(tpdf_source))

epdf_source = $(eps_source:.eps=.pdf)
pdf_source += $(epdf_source)

words=$(shell texcount -v3 -merge -incbib -dir -sub=none -utf8 -sum paper.tex | grep "Sum count")

paper.pdf: paper.tex  $(png_source) $(pdf_source)
	pdflatex paper.tex < /dev/null
	bibtex paper < /dev/null
	pdflatex paper.tex < /dev/null
	pdflatex paper.tex < /dev/null
	pdflatex paper.tex < /dev/null
	@echo "estimate of number of words: " $(words)

pdf:	paper.pdf 

%.pdf: %.eps
	$(EPStoPDF) $<

clean:
	$(RM) $(epdf_source) paper.dvi 
	$(RM) paper.blg paper.log
	$(RM) paper.aux paper.ps paper.bbl
	$(RM) *~

.PHONY: clean
