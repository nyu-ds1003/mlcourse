TARGET = 01a.overview.pdf \
		 01b.intro-machine-learning.pdf \
		 01c.intro-stat-learning-theory.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<
	open $@

main: $(TARGET) 

clean:
	rm *.aux *.log *.nav *.out *.snm *.toc *.pdf

