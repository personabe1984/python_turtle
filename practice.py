import turtle


loadWindow = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    turtle.color(2*i, 2*i, 2*i)

turtle.exitonclick()



def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)


for i in range(100):
    shape(5*i, sides)
    turtle.left(i) 
