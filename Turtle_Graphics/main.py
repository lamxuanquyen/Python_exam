import turtle
import time

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.title("qyn2512")
turtle.speed(0) #speed nhanh nhat
turtle.pensize(2)
time.sleep(5)
colors = ["red","white","blue","yellow","green","magenta"]
color_numer = len(colors)
for i in range(0,200,1): #loop from 0 to 199, step 1
    t.pencolor(colors[i%color_numer])
    t.forward(i)
    #t.left(360/color_numer + 1)
    t.left(360/color_numer - 1)

t.hideturtle()
turtle.mainloop()