import turtle

#Setup
t=turtle.Turtle()
t.speed(10)
LoadWindow=turtle.Screen()
LoadWindow.setup(width=1000,height=1000)
LoadWindow.title('Sequare Fractal')

#Fractal Shape
def build(h):
    i = 5
    i2 = 5
    t.pencolor('#3399ff')

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

    #Builds triangle
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

#Recursive function
def seq_frac(h):
    if h>h/8:   #Base case
        build(h)
        h/=2    #Change
        seq_frac(h) #Calls itself
    else:
        pass

print(seq_frac(300))

LoadWindow.exitonclick()