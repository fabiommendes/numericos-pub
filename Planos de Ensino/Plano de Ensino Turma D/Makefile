TARGET = Plano_de_Ensino.pdf

LATEX  = latex
DVIPS  = dvips
PS2PDF = ps2pdf

BASE_DIR = /home/edson/Aulas/2014_02/CB
INSTALL_DIR = build/docs/

MAIN_FILE = main.tex
DVI_FILE  = $(addsuffix .dvi, $(basename $(MAIN_FILE)))
PS_FILE   = $(addsuffix .ps, $(basename $(MAIN_FILE)))
PDF_FILE  = $(addsuffix .pdf, $(basename $(MAIN_FILE)))

SOURCES = 				\
	logo.tex 			\
	header.tex 			\
	objetivos.tex		\
	ementa.tex 			\
	horario.tex 		\
	metodologia.tex 	\
	criterios.tex 		\
	cronograma.tex 		\
	bibliografia.tex

.PHONY: all

all: 
	@make $(TARGET)
     
$(TARGET): $(MAIN_FILE) $(SOURCES)
	$(LATEX) $<
	$(DVIPS) $(DVI_FILE)
	$(PS2PDF) $(PS_FILE)
	@cp $(PDF_FILE) $(TARGET)

install: $(TARGET)
	@mkdir -p $(BASE_DIR)/$(INSTALL_DIR)
	@cp $< $(BASE_DIR)/$(INSTALL_DIR)
clean:
	@rm -f *~ $(PDF_FILE) *.dvi $(PS_FILE) *.backup *.aux *.log *.pyc

dist-clean: clean
	@rm -f $(TARGET)
