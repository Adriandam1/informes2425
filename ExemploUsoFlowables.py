
import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas

follaEstilo = getSampleStyleSheet()
estilo = follaEstilo['BodyText']

parragrafo = Paragraph("O texto que imos mostrar máis lonxitude haber si  para que non entre temos que escribir máis e máis textotexto")

obxetoCanvas = Canvas(os.path.realpath('PDF/exemploFlowable.pdf'))
# esto e unha tupla:
ancho, alto = 300, 300

anchoAux, altoAux = parragrafo.wrap(ancho, alto)
print(str(anchoAux)+ " "+ str(altoAux))

if anchoAux <= ancho and altoAux <= alto:
    ancho = ancho - anchoAux
    parragrafo.drawOn(obxetoCanvas, 0, altoAux)
    obxetoCanvas.save()
else:
    raise ValueError("Non hai espazo suficiente")
