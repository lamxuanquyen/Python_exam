import turtle 
tr = turtle.Turtle()
r = 10
distance_Input = input('Ban muon nhap khoang cach bao nhieu? :')

a=0
while(True):
    tr.circle(r+a, 45)
    a +=1
    if turtle.distance(tr.pos()) > int(distance_Input):
        break
    
turtle.done()
turtle.mainloop()