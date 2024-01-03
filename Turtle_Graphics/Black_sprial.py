import turtle

t =turtle.Turtle()
#t.pencolor("green")
t.speed(0)
a=1

while True :
    t.forward(a)
    t.left(120)
    t.left(1)
    a +=1
    if a == 1000:
        break
    t.hideturtle()

turtle.done()
