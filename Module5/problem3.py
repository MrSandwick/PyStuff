# Baatyrbek Turatov
# 5/13/2025
# Program uses turtle to draw a polyhedron which sides and length determined by user

import turtle

a = turtle.Screen()
b = turtle.Turtle()
userSides = input("Hi, please enter your number of sides")
userLength = input("Now, length of sides")
angle = 360.0 / userSides
for i in range(userSides):
    turtle.forward(userLength)
    turtle.right(angle)
turtle.done()