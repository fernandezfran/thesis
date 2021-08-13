COMPILER = pdflatex
CFLAGS = 

TARGETS = tesis

all: $(TARGETS)

tesis: tesis.tex
	$(COMPILER) $(CFLAGS) $<

clean:
	rm -f *.aux *.log *.out $(TARGETS)

.PHONY: clean all
