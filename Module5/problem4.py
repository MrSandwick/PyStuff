# Baatyrbek Turatov
# 5/13/2025
# Program create an array with numbers from 1 to 50 and checks if these numbers are multiples of 3, 5 or both.

nums = [i for i in range(1, 51)]
for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} divisible by both 3 & 5")
    elif num % 5 == 0:
        print(f"{num} divisible by 5")
    elif num % 3 == 0:
        print(f"{num} divisible by 3")