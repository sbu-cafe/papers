ALL: astronum-maestroex.pdf

PNGS := $(wildcard *.png)
PDFS := $(filter-out astronum-maestroex.pdf,$(wildcard *.pdf))

astronum-maestroex.pdf: astronum-maestroex.tex ws.bib $(PNGS) $(PDFS)
	pdflatex astronum-maestroex
	bibtex astronum-maestroex
	pdflatex astronum-maestroex
	pdflatex astronum-maestroex


clean: 
	rm -f astronum-maestroex.aux astronum-maestroex.log astronum-maestroex.bbl astronum-maestroex.blg

realclean: clean
	rm -f astronum-maestroex.pdf
