import os.path

from reportlab.graphics.shapes import Drawing
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
from reportlab.graphics.charts.legends import LineLegend
from reportlab.graphics.charts.textlabels import Label

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







# showBoundary lle fai un recuadro
doc = SimpleDocTemplate("ExemploGraficas.pdf", pagesize=A4, showBoundary= 1)
doc.build(documento)
