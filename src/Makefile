# Copyright (c) 2024, Francisco Fernandez
# License: CC BY-SA 4.0
#   https://github.com/fernandezfran/thesis/blob/main/LICENSE
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
