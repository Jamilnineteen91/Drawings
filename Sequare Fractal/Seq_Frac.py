import turtle

#Setup
t=turtle.Turtle()
t.speed(9)
LoadWindow=turtle.Screen()
LoadWindow.setup(width=1000,height=1000)
LoadWindow.title('Sequare Fractal')

#Builds shape; North-South
def y_axis_build(h):
    i = 5
    i2 = 5
    t.pencolor('#6600ff')

    #Builds triangle
    t.penup()
    t.goto(-h,0)
    t.pendown()
    t.goto(0,h)
    t.goto(h,0)

    #Builds lines
    while i<h:
        t.penup()
        t.goto(-h+i,i)
        t.pendown()
        t.goto(i,h-i)
        i+=5

    # Builds triangle
    t.penup()
    t.goto(-h,0)
    t.pendown()
    t.goto(0,-h)
    t.goto(h,0)

    #Builds lines
    while i2<h:
        t.penup()
        t.goto(-h+i2,-i2)
        t.pendown()
        t.goto(i2,-h+i2)
        i2+=5

#Builds shape; West-East
def x_axis_build(h):
    i=5
    i2=5
    t.pencolor('#2eb82e')

    # Builds triangle
    t.penup()
    t.goto(0,-h)
    t.pendown()
    t.goto(h,0)
    t.goto(0,h)

    #Builds lines
    while i<h:
        t.penup()
        t.goto(i, (-h)+i)
        t.pendown()
        t.goto((h)-i, i)
        i += 5

    # Builds triangle
    t.penup()
    t.goto(0,-h)
    t.pendown()
    t.goto(-h,0)
    t.goto(0,h)

    #Builds lines
    while i2<h:
        t.penup()
        t.goto(-i2,(-h)+i2)
        t.pendown()
        t.goto((-h)+i2, i2)
        i2+= 5

def seq_frac(h):

    y_axis_build(h)
    x_axis_build(h/2)
    y_axis_build(h/4)
    x_axis_build(h/8)

print(seq_frac(300))


LoadWindow.exitonclick()