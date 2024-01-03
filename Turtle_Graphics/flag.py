import turtle as t
import math
import time

def draw_rectangle(horizontal, vertical, color,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for i in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.right(angle)
        t.forward(size)
        #t.right(angle)
    t.end_fill()

# Main code
t.Screen().bgcolor('dark blue')
t.title("QYN2512")
t.speed(1)
time.sleep(5)

chieudai_HCN = 600
chieurong_HCN = (chieudai_HCN*2)/3
x_rectangle = -(chieudai_HCN/2)
y_rectangle = chieurong_HCN/2
draw_rectangle(chieudai_HCN, chieurong_HCN, 'red', x_rectangle, y_rectangle)
#draw_rectangle(chieudai, chieurong, 'red',-150,100)

wing_star = 5
x_star = (chieudai_HCN/wing_star)* (math.cos((90/wing_star)/180*math.pi))
y_star = (chieudai_HCN/wing_star)* (math.sin((90/wing_star)/180*math.pi))
#dùng cos,sin thì phải đổi độ sang radian
#print(x_star, y_star)
size_star = 2* x_star
draw_star(wing_star, size_star, 'yellow', x_star, y_star)
#draw_star(5, 114, 'yellow', 57, 19)

t.hideturtle()
t.mainloop()