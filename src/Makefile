# https://mg.readthedocs.io/latexmk.html
COMPILER = latexmk
thesis_flags = -pdf -pdflatex="pdflatex" -use-make -quiet
clean_flags = -c

TARGETS = thesis

all: $(TARGETS)

thesis: thesis.tex
	$(COMPILER) $(thesis_flags) $<

clean:
	$(COMPILER) $(clean_flags)

.PHONY: clean all
