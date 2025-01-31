
from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

# creamos una lista que luego le pasaremos al renderizador
guion = []
# widt y height son las dimensiones en pixeles
imaxe = Image (400, 0, 180, 175, "/home/dam/Desktop/Descargas/tick.png")
# creamos un debuxo coas dimensions e lle incorporamos a imaxe
debuxo = Drawing ( 50, 30) # creamos obxeto drawing
debuxo.add(imaxe) # incluiomos o obxeto drawing na imaxe
# podemos decirlle do punto orixinal, canto vai a desprazar
debuxo.translate(0, 500)
guion.append(debuxo)

debuxo = Drawing (50, 30)
debuxo.add(imaxe)
debuxo.rotate(90) # rotar o debuxo
debuxo.scale(1.5, 1) # escalar o debuxo
debuxo.translate(-400, -500) # podemos mover o debuxo
guion.append(debuxo) # añadimos o debuxo otra vez depois de modificalo

debuxo = Drawing(50, 30)
debuxo.add(imaxe)
debuxo.rotate(45)
debuxo.translate(-40, 100)
guion.append(debuxo)

#creamos co as dimensions A4
debuxo = Drawing (A4[0], A4[1])
# recorremos a lista e lle engadimos os elementos
for elemento in guion:
    debuxo.add(elemento)

# por ultimo utilizamos renderPDF facemos outro drawTOFilre e lle decimos que o ultimo debuxo e o que incorpora todos os demais
renderPDF.drawToFile(debuxo, "probaConDrawingImage.pdf")


















