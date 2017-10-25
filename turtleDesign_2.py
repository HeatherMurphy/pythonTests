import turtle
x=5 #distance defined
t=0  #tilt defined
c= 0  #cursor position defined lateral
c2= 0 #cursor position defined vertical
t=0 #defining tilt
turtle.hideturtle()
turtle.penup ()
turtle.speed (20)
turtle.pencolor('red')
turtle.pensize(3)
turtle.bgcolor('gray')
while (x < 400):
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.right(90+t)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.end_fill()
    turtle.penup ()
    turtle.goto(c, c2)
    turtle.pendown ()
    x=x+10
    c=c+5
    c2=c2+5
    t=t+.5
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.write('SUCCESS!')

 
 
