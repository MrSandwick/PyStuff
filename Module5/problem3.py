# Baatyrbek Turatov
# 5/13/2025
# Program uses turtle to draw a polyhedron which sides and length determined by user

# !!!I get it now, terminal does not updating itself because of turtle screen. 
# It creates a turtle screen but it's not showing above all other open windows. How do I fix it?

import turtle

while True:
    try:
        userSides = int(input("Hi, please enter your number of sides\n"))
        userLength = int(input("Now, length of sides\n"))
        
        if userSides >=3 and userLength >0:
            break
        else: 
            turtle.bye()
            print("Please enter valid values")
            exit()
        
    except (TypeError, ValueError):
        turtle.bye()
        print("Only numbers are valid")
        exit()


a = turtle.Screen()
b = turtle.Turtle()

angle = 360.0 / userSides
for i in range(userSides):
    turtle.forward(userLength)
    turtle.right(angle)
turtle.done()