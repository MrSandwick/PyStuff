# Baartyrbek Turatov 
# 5/21/2025

# Problem 1: Use a for statement and random.randrange to print 10 random integers between 25 and 35. 

import random

randInt = [random.randint(25, 35) for _ in range(10)]
print(randInt)