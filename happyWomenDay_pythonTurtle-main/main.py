import turtle
from turtle import Turtle, Screen, Shape
import time
from tkinter import PhotoImage



t = turtle.Turtle()
t.shape("turtle")
t.color("pink")
t.fillcolor('green')


screen = turtle.Screen()
turtle.title("Developed by Hoang Thuc")
widths = turtle.window_width()
heights = turtle.window_height()
screen.setup(500, 500)
# screen.bgpic("background.gif")
draw_speed = t.speed(2)
pen_size = t.pensize(8)


def setUpTheme(themeColor):
    screen.bgcolor(themeColor)
    # t.color('pink')        # cursor line color
    t.fillcolor('red')      # filled heart & cursor
    t.begin_fill()


def setUpPosition():
    # t.ht()
    draw_speed
    pen_size
    t.up()
    t.goto(0,-130)
    t.down()


def leftHeart():
    time.sleep(0.5)
    draw_speed
    pen_size
    t.down()
    t.left(140)
    t.forward(180)
    t.circle(-90,200)
    t.up()


def rightHeart():
    # t.ht()
    time.sleep(0.5)
    draw_speed
    pen_size
    t.down()          # start pen
    t.circle(-90,200)
    t.forward(180)
    draw_speed
    t.end_fill()      # fill the heart with color
    t.up()         


def textContent(content_1,content_2,content_3,color,font_1, font_2, fontSize):
    t.setpos(-157,30)   # text position
    t.color(color)

    time.sleep(1.2)
    t.write(content_1, font=(font_1, fontSize, 'bold'))
    t.setpos(-65,-15)
    time.sleep(1.2)
    t.write(content_2, font=(font_1, fontSize, "bold"))
    time.sleep(1.2)
    t.setpos(-160,-190)
    # t.down()
    t.write(content_3, font=(font_2, fontSize, "bold"))
    time.sleep(1.2)


if __name__ == "__main__":
    # t.ht()              # hide cursor
    setUpTheme("black")
    setUpPosition()
    leftHeart()
    t.setheading(60)      # upper crossing point
    rightHeart()

    t.ht()
    textContent(
        "Happy Women's Day", "Thu Liễu",
        "Luôn Vui Vẻ Và Xinh Đẹp Nha",
        "lightgreen", "Verdana",
        "Calibri", 20
        )
    time.sleep(1)
    screen.clear()
    screen.bgpic("background.gif")
    turtle.mainloop()
    turtle.bye()
    screen.exitonclick()