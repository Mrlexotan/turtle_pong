import os
import turtle

# Janela do jogo
window = turtle.Screen()
window.setup(1200, 800)
window.title("Turtle Pong")
window.bgcolor("black")

# player1
player1 = turtle.Turtle()
player1.penup()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.goto(-500, 0)
player1.shapesize(8, 1)

# player2
player2 = turtle.Turtle()
player2.penup()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.goto(500, 0)
player2.shapesize(8, 1)

# ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.goto(0, 0)
ball.shapesize(1, 1)


# define o movimento de subida do player1
def up():
    y = player1.ycor()
    y += 10
    player1.sety(y)

    if player1.ycor() >= 320:
        player1.sety(320)


# define o movimento de descida do player1
def down():
    y = player1.ycor()
    y -= 10
    player1.sety(y)

    if player1.ycor() <= -320:
        player1.sety(-320)


# define o movimento de subida do player2
def up2():
    y = player2.ycor()
    y += 10
    player2.sety(y)

    if player2.ycor() >= 320:
        player2.sety(320)


# define o movimento de descida do player2
def down2():
    y = player2.ycor()
    y -= 10
    player2.sety(y)

    if player2.ycor() <= -320:
        player2.sety(-320)


# adicionando os controles do player1
window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")

# adicionando os controles do player2
window.listen()
window.onkeypress(up2, "i")
window.onkeypress(down2, "k")

# Mantém a janela aberta
loop = True
while loop:
    window.update()
