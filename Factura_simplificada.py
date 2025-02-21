
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, BaseDocTemplate, PageTemplate, Frame, Spacer, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Image
from reportlab.lib import colors

from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.styles import ParagraphStyle

# -------------------------------------------------

# -------------------------------------------------



follaEstilo = getSampleStyleSheet()
documento = []
estilo = follaEstilo['BodyText']

documento.append(Spacer(0, 20)) # espacio borde superior


# ----------------------------------------
# Titulo factura simplificada

factura = ParagraphStyle(name='RightAligned', parent=follaEstilo['BodyText'], alignment=TA_RIGHT, textColor = colors.darkgreen, fontName = 'Helvetica-Bold', fontSize=14)
paragrafo = Paragraph("FACTURA SIMPLIFICADA", factura)

documento.append(paragrafo)
documento.append(Spacer(0, 20))

# ----------------------------------------
# Nombre de tu Empresa                 Logo de la Empresa
# Dirección
# Ciudad y País
# CIF/NIF                      Fecha Emisión    DD/MM/AAAA
# Teléfono                 Numero de factura    A0001
# Mail

# Información de la empresa y logo
empresa_info = [
    ['Nombre de tu Empresa', '', 'Logo de la Empresa', ''],
    ['Dirección', '', '', ''],
    ['Ciudad y País', '', '', ''],
    ['CIF/NIF', '', 'Fecha Emisión', 'DD/MM/AAAA'],
    ['Teléfono', '', 'Número de factura', 'A0001'],
    ['Mail', '', '', '']
]

# Ajustar el ancho de las columnas
colWidths = [250, 90, 90, 90]  # Ancho de cada columna en puntos
rowHeights = [40] + [None] * 5  # Ajustar la altura de la última fila


# Definir estilos
estilo_empresa = TableStyle([
    ('SPAN', (2, 0), (3, 0)),  # Combina las celdas 2 y 3 de la primera fila
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alinea el contenido a la izquierda
    ('ALIGN', (2, 0), (3, 0), 'RIGHT'),  # ALinea logo de la empresa a la derecha
    ('ALIGN', (-1, 3), (-1, 4), 'LEFT'),
    ('ALIGN', (0, 0), (0, 5), 'LEFT'), # Logo de la empresa a la izquierda
    ('ALIGN', (2, 3), (2, 3), 'RIGHT'),  # Alinea la fecha a la derecha
    ('ALIGN', (3, 3), (3, 3), 'CENTER'),  # Alinea el número de factura a la derecha
    ('ALIGN', (3, 4), (3, 4), 'CENTER'),  # Alinea el número de factura a la izquierda
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Alinea verticalmente al medio
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkgreen), # Color del texto verde oscuro
    ('FONT', (0, 0), (-1, -1), 'Helvetica-Bold'), # Toda taboa negrita
    ('FONT', (0, 1), (0, -1), 'Helvetica-BoldOblique'),  # Negrita cursiva primera columna
    ('FONTSIZE', (0, 0), (0, 0), 20), # Tamaño letra Nombre de tu empresa
    ('FONTSIZE', (2, 0), (3, 0), 16), # Tamaño letra Logo de empresa
    #('FONTSTYLE', (0, 0), (-1, -1), 'BOLD'),
])

tabla_empresa = Table(data=empresa_info, style=estilo_empresa, colWidths=colWidths, rowHeights=rowHeights)
documento.append(tabla_empresa)
documento.append(Spacer(0, 20))


# ----------------------------------------
# Tabla de productos

cabecera = ['Descripción', 'Importe', 'Cantidad', 'Total']
fila1 = ['Producto1', '3,2', '5', '16']
fila2 = ['Producto2', '2,1', '3', '6,30']
fila3 = ['Producto3', '2,9', '76', '220,40']
fila4 = ['Producto4', '5', '23', '115,00']
fila5 = ['Producto5', '4,95', '3', '14,85']
fila6 = ['Producto6', '6', '2', '12.00']
filaEnBlanco = ['', '', '', '']
total = ['', '', 'TOTAL', '385 €']

datos = [cabecera, fila1, fila2, fila3, fila4, fila5, fila6,filaEnBlanco, total]

# Ajustar el ancho de las columnas
colWidths = [250, 90, 90, 90]  # Ancho de cada columna en puntos
rowHeights = [None] * 7 + [8] + [30]  # Ajustar la altura de la última fila
# Definir estilos

# Crear un color verde muy clarito y pálido para el fondo de los productos
verde_clarito = colors.Color(red=0.9, green=1.0, blue=0.9)

estilo_tabla = [
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, 1), (-1, -2), verde_clarito),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN', (3, 1), (-1, -2), 'RIGHT'),
    ('FONT', (0, 0), (3, 0), 'Helvetica-Bold'),  # negrita linea 0
    ('GRID', (0, 0), (-1, -1), 1, colors.white),
    ('BACKGROUND', (0, 7), (-1, 7), colors.white),
    ('BACKGROUND', (2, 8), (-1, -1), colors.darkgreen),
    ('TEXTCOLOR', (2, 8), (-1, -1), colors.white),
    ('FONTSIZE', (2, 8), (-1, -1), 12),
    ('FONT', (2, 8), (-1, -1), 'Helvetica-Bold'),  # negrita linea 0
    ('ALIGN', (2, 8), (-1, -1), 'CENTER'),
]

tabla = Table(data=datos, style=estilo_tabla, colWidths=colWidths, rowHeights=rowHeights)
documento.append(tabla)

# ----------------------------------------

# COLUMNA VERDE -----------------------
# Función para dibujar la columna verde a la izquierda del documento
# esto nos fuerza a ponerle un margen izquierdo al fram de +1*cm para que no se superpongan
# tambien debemos añadirlo con onPage=draw_background en el addPageTemplates
def draw_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.mediumseagreen)
    canvas.rect(0, 0, 2*cm, A4[1], fill=1)
    canvas.restoreState()

# Crear el documento PDF
doc = BaseDocTemplate("PDF/Factura_simplificada.pdf", pagesize=A4)
# Definir el marco de la página
frame = Frame(doc.leftMargin +1*cm, doc.bottomMargin, doc.width, doc.height, id='normal')
# Añadir la plantilla de página
template = PageTemplate(id='test', frames=frame, onPage=draw_background)
doc.addPageTemplates([template])
# Construir el documento
doc.build(documento)


"""
# showBoundary lle fai un recuadro
doc = SimpleDocTemplate("Factura_simplificada.pdf", pagesize=A4, showBoundary= 1)
doc.build(documento)
"""
