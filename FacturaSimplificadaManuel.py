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

#PARA BASE DE DATOS MANUEL ESTA HACIENDO EL EJEMPLO FACTURA2
import sqlite3 as dbapi

marxeSup = A4[1] - 2*cm
marxeInf = 1.5*cm
marxeEsq = 3*cm
marxeDer = A4[0] - 1.5*cm
anchoPaxina = marxeDer - marxeEsq

bbddfac2 = dbapi.connect("bbddfac2.dat")
cursor = bbddfac2.cursor()
cursor.execute("""Select id_factura, fecha_emision, id_empresa, numero_factura from Factura""")

logo = []
facturas = []
for factura in cursor.fetchall():
    facturas.append (factura)

# Estamos con la esquina superior derecha
for i, factura in enumerate (facturas):
    c = Canvas('facturaNum' + str(i)+'.pdf', pagesize=A4) # creo un canva por cada factura, si quisexemes 2 facturas por paxina usariamos A2
    logo.append(Image ("tick.png", 100, 55))
    frmLogo =   Frame (marxeDer-100, marxeSup-55, 100, 70, showBoundary=0)
    frmLogo.addFromList(logo, c) # lle digo que utilize a lista sobre o canvas
    tx = c.beginText(marxeDer-105, marxeSup-60) # creo un obxeto texto que o situei debaixo do logo
    tx.setFont("Helvetica", 14)
    tx.textLine("Electropachachos")
    c.drawText(tx) # estamos pintando  o texto no canvas

    frmDatosFactura = Frame (marxeDer -100, marxeSup -120, 90, 50, showBoundary=0)
    tblDatosFact = Table (data= (('Data de emisión: ', factura[1]), ('Número factura: '. factura[3])))
    frmDatosFactura.addFromList(list().append(tblDatosFact), c) # creo unha lista e lle engado un elemento e lle paso o canvas para que o rexistre ahi


    cursor.execute("""Select nome, direccion, cidade, pais, email, cid_nif, telefono From Empresa Where id_empresa = ?""", (factura[2],))
    # frmDatosCliente =
    # tblDatosCliente

    # Manuel retoma y coge codigo que ya tiene hecho, lo hemos perdido
    # pedir a manuel por que reengancharle va a ser imposible













































