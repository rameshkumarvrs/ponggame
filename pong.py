
import turtle



win = turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("pong game")

#left paddle
left_padel = turtle.Turtle()
left_padel.speed(0)
left_padel.shape("square")
left_padel.color("white")
left_padel.shapesize(stretch_wid=5, stretch_len=1)
left_padel.penup()
left_padel.goto(-380,0)

while True:
    win.update()