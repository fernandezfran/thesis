COMPILER = latexmk
tesis_flags = -pdf -quiet 
clean_flags = -c

TARGETS = tesis

all: $(TARGETS)

tesis: tesis.tex
	$(COMPILER) $(tesis_flags) $<

clean:
	$(COMPILER) $(clean_flags)
	rm *.bbl

.PHONY: clean all
