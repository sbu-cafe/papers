ALL: astronum-castro-2019.pdf

PNGS := $(wildcard *.png)
PDFS := $(filter-out astronum-castro-2019.pdf,$(wildcard *.pdf))

astronum-castro-2019.pdf: astronum-castro-2019.tex ws.bib $(PNGS) $(PDFS)
	pdflatex $<
	bibtex $(subst .tex,,$<)
	pdflatex $<
	pdflatex $<


clean: 
	rm -f astronum-castro-2019.aux astronum-castro-2019.log astronum-castro-2019.bbl astronum-castro-2019.blg

realclean: clean
	rm -f astronum-castro-2019.pdf
