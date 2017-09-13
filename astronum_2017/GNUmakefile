ALL: astronum-amrex.pdf

PNGS := $(wildcard *.png)

astronum-amrex.pdf: astronum-amrex.tex ws.bib $(PNGS)
	pdflatex astronum-amrex
	bibtex astronum-amrex
	pdflatex astronum-amrex
	pdflatex astronum-amrex


clean: 
	rm -f astronum-amrex.aux astronum-amrex.log astronum-amrex.bbl astronum-amrex.blg

realclean: clean
	rm -f astronum-amrex.pdf
