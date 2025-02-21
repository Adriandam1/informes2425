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
# reportlab tables: https://docs.reportlab.com/reportlab/userguide/ch7_tables/

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
# crear unha taboa
documento.append(Spacer (0, 20))

# AGORA FACEMOS UNHA TABOA
# docu tables: https://docs.reportlab.com/reportlab/userguide/ch7_tables/
cabTaboa = ['', 'Luns', 'Martes', 'Mércores', 'Xoves', 'Venres', 'Sabado', 'Domingo']
manhan = ['Mañan', 'Estudar', 'Ximnasio', 'Estudar', 'Estudar', 'Correr', 'Estudar', 'Descansar']
tarde  = ['Tarde', 'Traballar', 'Traballar', 'Descanso', 'Traballar', 'Traballar', 'Descanso', 'Descanso']
noite = ['Noite', 'Descanso', 'Traballar', 'Descanso', 'Saír', 'Traballar', 'Descanso', 'Descanso']
#unha vez cos elementos da taboa creamos o obxeto table
taboa = Table([cabTaboa, manhan, tarde, noite])
# engadimos ao guion que tiñamos "documento"
documento.append(taboa)
#aplicamos stilos a taboa
# las posiciones se marcan como: COLUMNA, FILA
#en background utilizamos: as coordenadas da taboa de inicio e as coordenadas de fin (1,1), (-1, -1) e o color
taboa.setStyle([('BACKGROUND', (1,1), (-1, -1), colors.lightgrey )])
# con BOX poñemos contorno ou caixa, temos que por: coordenadas de taboa de inicio, final, tamaño do grosor da liña e color
taboa.setStyle([('BOX', (1,1), (-1, -1), 0.5, colors.darkgrey)])
# INNERGRID(malla interior) linea entre las posiciones de la taboa utilizamos: as coordenadas da taboa de inicio e as coordenadas de fin (1,1), (-1, -1) e o color
taboa.setStyle([('INNERGRID', (1,1), (-1, -1), 0.25, colors.white)])
# TEXTCOLOR cambia el colo del texto utilizamos: as coordenadas da taboa de inicio e as coordenadas de fin (1,1), (-1, -1) e o color
taboa.setStyle([('TEXTCOLOR', (0,0), (0, -1), colors.darkgrey)])
taboa.setStyle([('TEXTCOLOR', (1,0), (-1, 0), colors.darkgrey)])

documento.append(Spacer (0, 20))

# CREAMOS UNHA NOVA TABOA
datos = [['Esquina sup', '', '02', '03', '04' ],
         ['', '', '12', '13', '14'],
         ['20', '21', '22', 'Esquina inf', ''],
         ['30', '31', '32', '', '']]
# SPAN = une celdas de una posicion de inicio a una final
# VALIGN alinea o texto por exemplo no centro MIDDLE
# ALIGN centra el texto
estilo = [('LINEABOVE', (0,0), (-1,-1), 1, colors.blue),
          ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
          ('BACKGROUND', (0,0), (1,1), colors.lavenderblush),
          ('SPAN', (0,0), (1,1)),
          ('BACKGROUND', (-2,-2), (-1,-1), colors.bisque),
          ('SPAN', (3,2), (-1,-1)),
          ('LINEBELOW', (0,-1), (-1,-1), 1, colors.blue),
          ('VALIGN', (0,0), (1,1), 'MIDDLE'),
          ('VALIGN', (-2,-2), (-1,-1), 'MIDDLE'),
          ('ALIGN', (0,0), (-1,-1), 'CENTER')
          ]
# creamos a taboa engadindo os datos e os estilos directamente no constructor
taboa2 = Table(data=datos, style=estilo)
documento.append(taboa2)
documento.append(Spacer (0, 20))

# Taboa con formato dinamico, os valores cambian segun xogemos coas variables
temperaturas = [['','Xan', 'Feb', 'Mar', 'Abr', 'Mai', 'Xun', 'Xul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec'],
                ['Máximas', 15, 16, 20, 25, 27, 31, 35, 38, 33, 25, 20, 18],
                ['Mínimas', -3, -4, -1, 5, 7, 9, 12, 15, 16, 10, 2, -1]
                ]
estilo = [('TEXTCOLOR', (0,0), (-1,0), colors.grey),
          ('TEXTCOLOR', (0,1), (0,-1), colors.grey),
          ('INNERGRID', (1,1), (-1,-1), 0.5, colors.white),
          ('BOX', (1,1), (-1,-1), 1.5,  colors.grey),
          ]
# facer un indice i, j para acceder aos datos
# collo as filas e lle dou valor 1,2
# collo as columnas e lle dou valores 1,2,3...
# neste caso comprobo que os valores das temperatuas son integer e poño condicions de valores
for i, fila in enumerate (temperaturas):
    for j, temperatura in enumerate(fila):
        if type (temperatura) == int:
            if temperatura > 0:
                estilo.append(('TEXTCOLOR', (j,i), (j,i), colors.black))
                if temperatura > 30:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.fidred))
                elif temperatura <= 30 and temperatura>= 20:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.orange))
                elif temperatura < 20 and temperatura >= 10:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
                elif temperatura < 10 and temperatura > 0:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
            else:
                estilo.append(('TEXTCOLOR', (j,i), (j,i), colors.blue))
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey))


taboa3 = Table(data=temperaturas, style=estilo)
documento.append(taboa3)






# showBoundary lle fai un recuadro
doc = SimpleDocTemplate("PDF/ExemploPLatypusTaboa.pdf", pagesize=A4, showBoundary= 1)
doc.build(documento)














