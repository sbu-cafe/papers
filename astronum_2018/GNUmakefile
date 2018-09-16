ALL: astronum-xrb.pdf

PNGS := $(wildcard *.png)
PDFS := $(filter-out astronum-xrb.pdf,$(wildcard *.pdf))

astronum-xrb.pdf: astronum-xrb.tex ws.bib $(PNGS) $(PDFS)
	pdflatex astronum-xrb
	bibtex astronum-xrb
	pdflatex astronum-xrb
	pdflatex astronum-xrb


clean: 
	rm -f astronum-xrb.aux astronum-xrb.log astronum-xrb.bbl astronum-xrb.blg

realclean: clean
	rm -f astronum-xrb.pdf
