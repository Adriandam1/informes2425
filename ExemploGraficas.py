import os.path

from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import yellow
# Para el ejemplo de graficas partimos del exmeplo platypus
# doc: https://docs.reportlab.com/reportlab/userguide/ch11_graphics/
# -------------------------------------------------
# -------------------------------------------------

from reportlab.platypus import SimpleDocTemplate

from reportlab.platypus import Spacer

#Importamos verticalbarcharts y demas para lñas graficas
from reportlab.graphics.charts.barcharts import VerticalBarChart3D, VerticalBarChart
#Importamos para grafica de liñas
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.piecharts import Pie, Pie3d

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

follaEstilo = getSampleStyleSheet() # mediante esta funcion obtemos a folla de estilo

# creamos unha lista para ir engadindo elementos
documento = []


# Taboa con formato dinamico, os valores cambian segun xogemos coas variables
temperaturas = [['','Xan', 'Feb', 'Mar', 'Abr', 'Mai', 'Xun', 'Xul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec'],
                ['Máximas', 15, 16, 20, 25, 27, 31, 35, 38, 33, 25, 20, 18],
                ['Mínimas', -3, -4, -1, 5, 7, 9, 12, 15, 16, 10, 2, -1]
                ]
# datos con coordenadas de puntos x y tupla con elementos
datos = [((1,1), (2,2), (2.5,2), (3,3.5), (4,7)),
         ((1,2), (2,3), (2.5,1), (3.5,3), (4,2))
         ]

# grafica normal ----------------------------------------

grafica = VerticalBarChart()
debuxo = Drawing(400, 200)
debuxo.add(grafica)
documento.append(Spacer(0, 20))
documento.append(debuxo)
# pòsicionamento no espazo para que non quede pegado
grafica.x = 50
grafica.y = 50
# lle podemos dar un tamaño
grafica.height = 125
grafica.width = 300
# definimos cousas para o aspecto
grafica.strokeColor = colors.black
# valor dos ejes valores minimo y maximo
grafica.valueAxis.valueMin = -10
grafica.valueAxis.valueMax = 50
# valor de salto
grafica.valueAxis.valueStep = 5
# podemos definir como se van a comportar as etiquetas que poñamos, por exemplo vamos a definir o anclaxe
# podemos elegir la orientacion de la estiquedas por exemplo 'ne' seria NorthEast, 'sw' seris SouthWest etc
grafica.categoryAxis.labels.boxAnchor = 'ne'
# podemos poñer un espazo en direccion x e direccion y, esas etiquetas que creamos, canto se van a instanciar
grafica.categoryAxis.labels.dx = 8
grafica.categoryAxis.labels.dy = -2
grafica.categoryAxis.labels.angle = 30
# como en temperaturas temos un primeiro valor en blanco(antes de 'Xan'), tenemos que facer un slicing [1:]
grafica.categoryAxis.categoryNames = temperaturas[0][1:]
# groupSpacing agrupa os datos e os separa entre grupos, neste caso entre temperatudas maximas e minimas
grafica.groupSpacing = 10
# barSpacing seria o mesmo perp para separar entre os meses
grafica.barSpacing = 2
# asignamos os datos, neste caso unha lista que engadiria temperatuas dende as filas 1 e 2 dous dende a columna 1 ao final
grafica.data = [temperaturas[1][1:], temperaturas[2][1:]]
# Cambiar el color de las barras de la grafica, cambiamos el color de la segunda fila(temperatuas minimas)
grafica.bars[1].fillColor = colors.blue
# cambiar a liña das series(el borde de las barras)
grafica.bars[1].strokeColor = colors.greenyellow

# grafica 3d ---------------------------------------------------------------------

grafica2 = VerticalBarChart3D()
debuxo = Drawing(400, 200)
debuxo.add(grafica2)
documento.append(Spacer(0, 20))
documento.append(debuxo)
# pòsicionamento no espazo para que non quede pegado
grafica2.x = 50
grafica2.y = 50
# lle podemos dar un tamaño
grafica2.height = 125
grafica2.width = 300
# definimos cousas para o aspecto
#grafica2.strokeColor = colors.black # En el 3d tenemos que quitar el marco de la grafica strokeColor por que sino EXPLOTA
# valor dos ejes valores minimo y maximo
grafica2.valueAxis.valueMin = -10
grafica2.valueAxis.valueMax = 50
# valor de salto
grafica2.valueAxis.valueStep = 5
# podemos definir como se van a comportar as etiquetas que poñamos, por exemplo vamos a definir o anclaxe
# podemos elegir la orientacion de la estiquedas por exemplo 'ne' seria NorthEast, 'sw' seris SouthWest etc
grafica2.categoryAxis.labels.boxAnchor = 'ne'
# podemos poñer un espazo en direccion x e direccion y, esas etiquetas que creamos, canto se van a instanciar
grafica2.categoryAxis.labels.dx = 8
grafica2.categoryAxis.labels.dy = -2
grafica2.categoryAxis.labels.angle = 30
# como en temperaturas temos un primeiro valor en blanco(antes de 'Xan'), tenemos que facer un slicing [1:]
grafica2.categoryAxis.categoryNames = temperaturas[0][1:]
# groupSpacing agrupa os datos e os separa entre grupos, neste caso entre temperatudas maximas e minimas
grafica2.groupSpacing = 10
# barSpacing seria o mesmo perp para separar entre os meses
grafica2.barSpacing = 2
# asignamos os datos, neste caso unha lista que engadiria temperatuas dende as filas 1 e 2 dous dende a columna 1 ao final
grafica2.data = [temperaturas[1][1:], temperaturas[2][1:]]
# Cambiar el color de las barras de la grafica, cambiamos el color de la segunda fila(temperatuas minimas)
grafica2.bars[1].fillColor = colors.blue
# cambiar a liña das series(el borde de las barras)
grafica2.bars[1].strokeColor = colors.greenyellow


# Grafica de liñas -------------------------------------
# Creamos unha nova grafica cos mesmos datos en forma de liñas en lugar de barras
#preparaciones para o grafico:
debuxo = Drawing(400, 200)
graficoL = HorizontalLineChart()
debuxo.add(graficoL)
documento.append(debuxo)

graficoL.x = 30
graficoL.y =50
graficoL.height = 125
graficoL.width = 350
graficoL.data = [temperaturas[1][1:], temperaturas[2][1:]]
graficoL.categoryAxis.categoryNames = temperaturas[0][1:]
graficoL.categoryAxis.labels.boxAnchor = 'n' # horientacion norte
graficoL.valueAxis.valueMin = -10
graficoL.valueAxis.valueMax = 50
graficoL.valueAxis.valueStep = 10
#liña 0 = temperaturas maximas, cambiamos el grosor de la liña a 2
graficoL.lines[0].strokeWidth = 2
# marcar os puntos un circulito en la linea
graficoL.lines[0].symbol = makeMarker ('FilledCircle')
# cambiamos la linea 1 para distinguirla un pocd de la linea 2
graficoL.lines[1].strokeWidth = 1.5
# cambiamos el color de la linea
graficoL.lines[1].strokeColor = colors.blue



# Grafica con LinePlot--------------------------------------------
debuxo = Drawing(400, 200)
#--------------
etiqueta = Label()
etiqueta.setOrigin(175,195)
etiqueta.angle = 15
etiqueta.dx = 0
etiqueta.dy = -5
etiqueta.boxStrokeColor = colors.grey # podemos poñerlle un marco oo
etiqueta.setText('Unha gáfica\ncon dúas series')
debuxo.add(etiqueta)
#--------------

lp = LinePlot()
debuxo.add(lp)
#documento.append(debuxo)
# metemos os datos
lp.data = datos

lp.x = 30
lp.y =50
lp.height = 125
lp.width = 350
lp.joinedLines = 1
lp.fillColor = colors.lightsalmon
lp.lines[0].symbol = makeMarker('FilledCircle')
lp.lines[1].symbol = makeMarker('Circle')
lp.lineLabelFormat = '%2.0f'
lp.strokeColor = colors.gray
lp.xValueAxis.valueMin = 0
lp.xValueAxis.valueMax = 5
lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 8
# le decimoas como queremos que sean los saltos
lp.yValueAxis.valueSteps = [1,2,3,4,5,6]

# creamos un obxeo LineLegend para referencias las lineas del grafico. utilizamos las etiquetas para recoger los colores que usamos en el grafico
lenda = LineLegend()
lenda.fontName = 'Helvetica'
lenda.fontSize = 7
lenda.alignment = 'right'
lenda.x = 30
lenda.y = 20
lenda.columnMaximum = 2
etiquetas = ['Caso 1', 'Caso 2']
# o color ten que ir alineado co nome, para eso creamos unha lista onde poñemos o color que ten as liñas para a serie correspondente
lenda.colorNamePairs = [(lp.lines[i].strokeColor, etiquetas[i]) for i in range (len (lp.data))]

debuxo.add(lenda)
documento.append(debuxo)

#-----------------------------------------
#Gracia de tarta (pie)
# https://docs.reportlab.com/reportlab/userguide/ch11_graphics/#pie-charts
debuxo = Drawing (300, 200)
tarta = Pie()
# posicionamos a tarta
tarta.x = 60
tarta.y = 15
# como he unha tarta nos deberia facer falta poñerlle proporcions
#tarta.width = 170
#tarta.height = 170
# añadimos os datos
tarta.data = [8, 6, 2, 4, 7, 3]
# poñemos has etiquetas
tarta.labels = ["AD", "PMDM", "EIE", "SXE", "DI", "PSP"]
# No caso da tarta usamos slices que os as porcions da tarta
tarta.slices.strokeWidth = 0.5
# popout es la medida para separar la porcion de la tarta
tarta.slices[4].popout = 10
# strokeWidth: ancho de liña
tarta.slices[4].strokeWidth = 2
# strokeDashArray: porcion que ten de negro e de blanco [unidades de negro, unidades de blanco]
tarta.slices[4].strokeDashArray = [2,2]
tarta.slices[4].labelRadius = 1.75
tarta.slices[4].fontColor = colors.red
tarta.sideLabels = 1

# añadimos unha lenda a nosa tarta
lenda = Legend()
lenda.x = 250
lenda.y = 10
lenda.dx = 8
lenda.dy = 8
lenda.fontName = "Helvetica"
lenda.fontSize = 8
lenda.boxAnchor = 'n'
lenda.columnMaximum = 10
lenda.strokeWidth = 1
lenda.strokeColor = colors.black
lenda.deltax = 75
lenda.deltay = 10
lenda.autoXPadding = 5
lenda.yGap = 0
lenda.dxTextSpace = 5 # espazo entre caracteres
lenda.alignment = 'right' # alineamento do texto
lenda.dividerLines = 1|2|4 # liñas divisorias
lenda.dividerOffsY = 5
lenda.subCols.rpad = 30
#indicsmoa os colores
cores = [colors.red, colors.blue, colors.green, colors.orange, colors.yellow, colors.lavender]
# numeramos os colores e se llos pasamos a tarta e a lenda
for i, color in enumerate (cores):
    tarta.slices[i].fillColor = color

lenda.colorNamePairs = [(tarta.slices[i].fillColor, (tarta.labels[i][0:20], '%0.2f' % tarta.data[i])
                             ) for i in range (len (tarta.data))] # collemos o nome collemos de 0 a 20 caracteres, marcamos que vai con 2 decimais



debuxo.add(lenda)
debuxo.add(tarta)
documento.append(debuxo)


#-----------------------------------------TARTA 3D
# es la misma tarta pero en 3d
documento.append(Spacer(0, 20)) # spacer para separas as tartasw
#Gracia de tarta3d (pie)
# https://docs.reportlab.com/reportlab/userguide/ch11_graphics/#pie-charts
debuxo = Drawing (300, 200)
tarta2 = Pie3d()
# posicionamos a tarta
tarta2.x = 80
tarta2.y = 0
# como he unha tarta nos deberia facer falta poñerlle proporcions
tarta2.width = 150
tarta2.height = 100
# añadimos os datos
tarta2.data = [8, 6, 2, 4, 7, 3]
# poñemos has etiquetas
tarta2.labels = ["AD", "PMDM", "EIE", "SXE", "DI", "PSP"]
# No caso da tarta usamos slices que os as porcions da tarta
tarta2.slices.strokeWidth = 0.5
# popout es la medida para separar la porcion de la tarta
tarta2.slices[4].popout = 10
# strokeWidth: ancho de liña
tarta2.slices[4].strokeWidth = 2
# strokeDashArray: porcion que ten de negro e de blanco [unidades de negro, unidades de blanco]
tarta2.slices[4].strokeDashArray = [2,2]
tarta2.slices[4].labelRadius = 1.75
tarta2.slices[4].fontColor = colors.red
tarta2.sideLabels = 1

# añadimos unha lenda a nosa tarta
lenda2 = Legend()
lenda2.x = 250
lenda2.y = 10
lenda2.dx = 8
lenda2.dy = 8
lenda2.fontName = "Helvetica"
lenda2.fontSize = 8
lenda2.boxAnchor = 'n'
lenda2.columnMaximum = 10
lenda2.strokeWidth = 1
lenda2.strokeColor = colors.black
lenda2.deltax = 75
lenda2.deltay = 10
lenda2.autoXPadding = 5
lenda2.yGap = 0
lenda2.dxTextSpace = 5 # espazo entre caracteres
lenda2.alignment = 'right' # alineamento do texto
lenda2.dividerLines = 1|2|4 # liñas divisorias
lenda2.dividerOffsY = 5
lenda2.subCols.rpad = 30
#indicsmoa os colores
cores = [colors.red, colors.blue, colors.green, colors.orange, colors.yellow, colors.lavender]
# numeramos os colores e se llos pasamos a tarta e a lenda
for i, color in enumerate (cores):
    tarta2.slices[i].fillColor = color

lenda2.colorNamePairs = [(tarta2.slices[i].fillColor, (tarta2.labels[i][0:20], '%0.2f' % tarta2.data[i])
                             ) for i in range (len (tarta2.data))] # collemos o nome collemos de 0 a 20 caracteres, marcamos que vai con 2 decimais



debuxo.add(lenda2)
debuxo.add(tarta2)
documento.append(debuxo)

#-------------------------------------------------




# showBoundary lle fai un recuadro
doc = SimpleDocTemplate("ExemploGraficas.pdf", pagesize=A4, showBoundary= 1)
doc.build(documento)
