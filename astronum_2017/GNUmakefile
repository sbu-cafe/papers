ALL: astronum-amrex.pdf

PNGS := $(wildcard *.png)
PDFS := $(filter-out astronum-amrex.pdf,$(wildcard *.pdf))

astronum-amrex.pdf: astronum-amrex.tex ws.bib $(PNGS) $(PDFS)
	pdflatex astronum-amrex
	bibtex astronum-amrex
	pdflatex astronum-amrex
	pdflatex astronum-amrex


clean: 
	rm -f astronum-amrex.aux astronum-amrex.log astronum-amrex.bbl astronum-amrex.blg

realclean: clean
	rm -f astronum-amrex.pdf
