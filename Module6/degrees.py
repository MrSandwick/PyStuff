# Baartyrbek Turatov 
# 5/21/2025

# Problem 5: 
# Search the internet for how to convert radians to degrees. 
# Write a program to compute the conversion given a user input value. 
# Print this value as well as the calculated value using the degrees function in the math module.

# For this we gonna use formula: degrees = radians × (180 / π). 
# Python's math module provides a convenient degrees() function for this conversion.


import math

# User input in radians
radianInput = float(input("Enter angle in radians: "))

# Manual conversion
degreesManual = radianInput * (180 / math.pi)

# Using math.degrees()
degreesBuiltin = math.degrees(radianInput)

print(f"Degrees (manual calculation): {degreesManual}")
print(f"Degrees (math.degrees function): {degreesBuiltin}")