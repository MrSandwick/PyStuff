# Baatyrbek Turatov
# 5/13/2025
# What the program does

import turtle
import random

screen = turtle.Screen()
b = turtle.Turtle()

length = 100
for i in range(1, 1000):
    r = random.randint(1, 360)
    turtle.forward(length)
    turtle.right(r)