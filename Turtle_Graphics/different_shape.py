import turtle
import time

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.title("qyn2512")
#turtle.pensize(5)
#t.speed(0)
time.sleep(5)
colors = ["red","white","blue","green","yellow","magenta"]
color_numer = len(colors)
vachmauthaydoi = 1
for i in range(0,200,1): 
    t.color(colors[i%color_numer])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(360/(color_numer + vachmauthaydoi) - 1)

t.hideturtle()
turtle.mainloop()