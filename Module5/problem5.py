# Baatyrbek Turatov
# 5/13/2025
# Program explores behavior of turtle under random effect
# P.S Not the most creative but I explored what people do with turtle, and it's just crazy lol

import turtle
import random

screen = turtle.Screen()
b = turtle.Turtle()

length = 100
for i in range(1, 1000):
    r = random.randint(1, 360)
    turtle.forward(length)
    turtle.right(r)