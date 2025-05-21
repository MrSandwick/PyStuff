# Baartyrbek Turatov 
# 5/21/2025

# Problem 6: 
# Use a for statement to calculate the factorial of a user input value. 
# Print this value as well as the calculated value using the factorial function in the math module.

# Factorial "n!" is the product of all positive integers starting from 1 till n


import math

# User input
number = int(input("Enter a non-negative integer: "))

# Factorial using for loop
factorialLoop = 1
for i in range(1, number + 1):
    factorialLoop *= i

# Factorial using math.factorial()
factorialBuiltin = math.factorial(number)

print(f"Factorial calculated using for loop: {factorialLoop}")
print(f"Factorial using math.factorial(): {factorialBuiltin}")