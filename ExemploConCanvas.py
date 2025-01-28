# Utilizando pdfgen
# obxecto Canvas (vai ser unha folla en branco que vamos a usar con coordenadas X e Y, as coordenadas 0.0 estan abajo izquierda)

from reportlab.pdfgen import canvas

papel = canvas.Canvas ("primeiroDocumento.pdf")
# tendo o obxeto en cambas pordemos usar unha serie de metodos:
# drawString permitenos "pintar" un texto onde lle indiquemos
papel.drawString(0, 0, "Posición orixinada (x,y) = (00, 00)")
papel.drawString(50, 100, "Posición orixinada (x,y) = (50, 100)")
papel.drawString(500, 700, "Posición orixinada (x,y) = (500, 700)")
# probamos a añadir unha imaxe
papel.drawImage("/home/dam/Desktop/tick.png", 200, 800, 20, 20 )
# el tamaño original del tick es 360 x 354 pixels, probamos con ese tamaño
papel.drawImage("../../Desktop/tick.png",100, 300, 360, 354)

# mostramos
papel.showPage()
# gardamos
papel.save()






















