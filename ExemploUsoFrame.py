
# O frame non seria mas que un area para conter elementos, parrafos, imaxes etc. E son os que contén a plantilla da paxina, o podemos ver como un espazo para debuxar
import os

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, Frame, Image, Spacer


obxectoCambas = Canvas (os.path.realpath('exemploUsoFrame.pdf'))
follaEstilo = getSampleStyleSheet()

estNormal = follaEstilo['Normal']
estCorpot = follaEstilo['BodyText']

documento =[]

imaxe = Image(os.path.relpath("/home/dam/Desktop/Descargas/tick.png"), width=90, height= 83)
documento.append(imaxe)
documento.append(Spacer (0, 20))

documento.append(Paragraph("O texto a mostrar no documento", estNormal))

# Creamos un frame medida, coordenadas de inicio, coordenadas de final
# (showBoundary es para enmarcar)
# margen, algo, posiciones, marco (REVISAR)
frame = Frame(cm, cm, 500, 400, showBoundary=1)
# le pasamos el documento, y el espacio para debuxar
frame.addFromList(documento, obxectoCambas)

doc2 = []
doc2.append(Paragraph("Segundo frame, distinto to primeiro", estCorpot))
doc2.append(Spacer(0, 20))
imaxe2 = Image(os.path.relpath("/home/dam/Desktop/Descargas/daniel.png"), width=180, height= 175)
doc2.append(imaxe2)

frame2 = Frame(3*cm, 450, 500, 300, cm, showBoundary=1)
frame2.addFromList(doc2, obxectoCambas)

obxectoCambas.save()
