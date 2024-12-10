
import turtle



win = turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("pong game")
win.tracer(0)

#left paddle
left_padel = turtle.Turtle()
left_padel.speed(0)
left_padel.shape("square")
left_padel.color("white")
left_padel.shapesize(stretch_wid=5, stretch_len=1)
left_padel.penup()
left_padel.goto(-380,0)


#right paddle
right_padel = turtle.Turtle()
right_padel.speed(0)
right_padel.shape("square")
right_padel.color("white")
right_padel.shapesize(stretch_wid=5, stretch_len=1)
right_padel.penup()
right_padel.goto(380,0)


#ball

bal = turtle.Turtle()
bal.speed(0)
bal.shape("circle")
bal.color("white")
bal.penup()
bal.dx = 0.10
bal.dy = 0.10


#moving paddles
def left_paddle_up():
	left_padel.sety(left_padel.ycor()+20)


def left_paddle_down():
		left_padel.sety(left_padel.ycor()-20)


def right_paddle_up():
		right_padel.sety(right_padel.ycor()+20)


def right_paddle_down():
		right_padel.sety(right_padel.ycor()-20)




win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 's')
win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')

while True:
    win.update()
    #ball movement

    bal.setx(bal.xcor()+bal.dx)
    bal.sety(bal.ycor()+bal.dy)
