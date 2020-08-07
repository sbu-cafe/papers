EPStoPDF = epstopdf

ALL: paper.pdf 

eps_source = $(wildcard *.eps)
png_source = $(wildcard *.png)

tpdf_source = $(wildcard *.pdf)
pdf_source = $(filter-out paper.pdf, $(tpdf_source))

epdf_source = $(eps_source:.eps=.pdf)
pdf_source += $(epdf_source)

paper.pdf: paper.tex  $(png_source) $(pdf_source)
	pdflatex paper.tex < /dev/null
	bibtex paper < /dev/null
	pdflatex paper.tex < /dev/null
	pdflatex paper.tex < /dev/null
	pdflatex paper.tex < /dev/null

pdf:	paper.pdf 

%.pdf: %.eps
	$(EPStoPDF) $<

clean:
	$(RM) $(epdf_source) paper.dvi 
	$(RM) paper.blg paper.log
	$(RM) paper.aux paper.ps paper.bbl
	$(RM) *~

.PHONY: clean
