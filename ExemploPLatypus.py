import os.path

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import Spacer
from reportlab.platypus import Table

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

#PLATYPUS = Page Layour And Typographic Using Stripes
# Reportlab userguide: https://docs.reportlab.com/rml/userguide/Chapter_1_Introduction/

follaEstilo = getSampleStyleSheet() # mediante esta funcion obtemos a folla de estilo

# creamos unha lista para ir engadindo elementos
documento = []

cabeceira = follaEstilo['Heading3']
cabeceira.pageBreakBefore = 0 # se lle poñemos 0 non nos vai facer salto de pagina tras escribir a cabeceira, si queremos deixar unha folla en branco podemos definilo (BUSCAR MAS INFO)
cabeceira.keepWithNext = 0
# backColor color de fondo
cabeceira.backColor = colors.lightgrey

# crearemos un parrafo e lle pasamos o estilo(cabeceira)
paragrafo = Paragraph("Cabeceira do documento", cabeceira)
documento.append(paragrafo) # añadimor o parrafo co estilo cabeceira o documento

# creo un texto e multilico 1000 veces
cadea = "Un texto que se vai a repetir múltiples veces e facer un volumnoso documento." * 1000

#definimos o estilo do paragrafo
estiloP = follaEstilo ['BodyText']
paragrafo = Paragraph(cadea, estiloP)
documento.append(paragrafo)
documento.append(Spacer(0, 20))

imaxe = Image(os.path.relpath("/home/dam/Desktop/Descargas/tick.png"), width=180, height= 175)
documento.append(imaxe)# metemos o elemento
#crear unha taboa
documento.append(Spacer (0, 20))
fila1 = ['', 'Luns', 'Martes', 'Mércores', 'Xoves', 'Venres', 'Sabado', 'Domingo']
manhan = ['Mañan', 'Estudar', 'Ximnasio', 'Estudar', 'Estudar', 'Correr', 'Estudar', 'Descansar']
tarde  = ['Tarde', 'Traballar', 'Traballar', 'Descanso', 'Traballar', 'Traballar', 'Descanso', 'Descanso']
noite = ['Noite', 'Descanso', 'Traballar', 'Descanso', 'Saír', 'Traballar', 'Descanso', 'Descanso']






# showBoundary lle fai un recuadro
doc = SimpleDocTemplate("ExemploPLatypus.pdf", pagesize=A4, showBoundary= 1)
doc.build(documento)














