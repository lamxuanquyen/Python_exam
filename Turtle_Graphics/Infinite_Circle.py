import turtle
import time

t= turtle.Turtle()

turtle.bgcolor("black")
turtle.title("qyn2512")
turtle.pensize(2)

time.sleep(5)
colors = ["red","white","blue","yellow","green","orange","magenta"]
soluongMau = len(colors)
soVonglap = 4
gocquay = 360 /(soluongMau*soVonglap)

for j in range(soVonglap):
    for i in colors:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(gocquay)

#góc quay=360/(số lượng màu*số vòng lặp) 

turtle.mainloop()