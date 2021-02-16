TARGET = 03a.feature-selection.pdf \
		 03b.regularization.pdf \
		 03c.lasso-optimization.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<
	open $@

main: $(TARGET) 

clean:
	rm *.aux *.log *.nav *.out *.snm *.toc *.pdf

