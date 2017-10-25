import turtle
x=5 #distance defined
t=0  #tilt defined
c= 0  #cursor position defined lateral
c2= 0 #cursor position defined vertical
t=0 #defining tilt
turtle.penup ()
turtle.speed (5)
turtle.pencolor('red')
while (x < 400):
    turtle.right(90+t)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.penup ()
    turtle.goto(c, c2)
    turtle.pendown ()
    x=x+10
    c=c+5
    c2=c2+5
    t=t+2
    
    
 
 
