from turtle import *

speed(30)

forward(200)
#we want to paint a house
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
left(90)

penup()
goto(200,200)
pendown()


color("red")
right(-120)
forward(200)
left(120)
forward(200)

color("black")
penup()
goto(30, 150)
pendown()

right(60)

forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)

penup()
goto(150, 150)
pendown()

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

exitonclick()