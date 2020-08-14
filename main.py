import os
import turtle

#Janela do jogo
window = turtle.Screen()
window.setup(1200, 800)
window.title("Turtle Pong")
window.bgcolor("black")

#player1
player1 = turtle.Turtle()



#Mantém a janela aberta
loop = True
while loop:
    window.update()