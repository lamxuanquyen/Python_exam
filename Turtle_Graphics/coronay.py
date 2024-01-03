import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("red")  
  
a = 0  
b = 0  
#t.speed(0)  
t.penup()  
t.goto(0,150)  
t.pendown()  
while(True):  
    t.forward(a)  
    t.right(b)  
    a+=2  
    b+=1
    #print(a,b)
    if b == 210:  
        break  
    t.hideturtle()  
  
turtle.done()