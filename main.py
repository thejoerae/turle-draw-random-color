from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
colormode(255)

for _ in range(3, 11):
    angle = int(360 / _)

    for draw in range(_ + 1):
        tim.forward(100)
        tim.right(angle)

    tim.color(random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255))

screen = Screen()
screen.exitonclick()
