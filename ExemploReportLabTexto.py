
from reportlab.pdfgen import canvas

cadea = ["Tres tristes tigres", "comeron trigo nun trigal", "en que trigal", "comeron os tristes tigres"]

aux = canvas.Canvas("PDF/probaTexto.pdf")
obxetoTexto = aux.beginText() # esta funcion beginText nos permite facer un obxeto que nos permite pintar texto
obxetoTexto.setTextOrigin(100, 800)
obxetoTexto.setFont("Courier", 14)
for linha in cadea:
    obxetoTexto.textLine(linha) # esto nos permite pinta unha liña de texto
obxetoTexto.setFillGray(0.5) # lle cambiamos o color para diferenciar
outroTexto = """Este é outro texto de
                mostra para probar as
                caracteristicas de
                debuxo de texto"""
obxetoTexto.textLines(outroTexto)

obxetoTexto.textLine("")
obxetoTexto.textLine("")
for tipo in aux.getAvailableFonts(): ## este metodo nos devuelve los tipos de fuente de letras
    obxetoTexto.setFont(tipo, 12)
    obxetoTexto.textLine(tipo + ": "+ cadea[0])

obxetoTexto.setFont("Helvetica", 12)
obxetoTexto.setFillColorRGB(0,0 ,256)
for linha in cadea: # textOut, se escribimos varias veces vai a escribir no mesmo sitio, polo que temos que movernos manualmente
    obxetoTexto.textOut(linha)
    obxetoTexto.moveCursor(20, 15) # para que non se superponga movermos o texto 20 horizontal y 15 vertical

obxetoTexto.setFillColorRGB(0,1 ,1)
espazoCar = 0
for linha in cadea:
    obxetoTexto.setCharSpace(espazoCar)
    obxetoTexto.textLine("Espazo %s : %s "% (espazoCar, linha))
    espazoCar+=1

obxetoTexto.setFillGray(0.7)
obxetoTexto.setCharSpace(0) # espacio entre letras (0 parece el standard)
obxetoTexto.setWordSpace(8) # espacio entre cada palabra
obxetoTexto.textLines(outroTexto)

#PLATYPUS = Page Layour And Typographic Using Stripes


aux.drawText(obxetoTexto)

aux.showPage()
aux.save()








