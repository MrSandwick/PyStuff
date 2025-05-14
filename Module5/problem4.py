# Baatyrbek Turatov
# 5/13/2025
# What the program does

nums = [i for i in range(1, 51)]
for num in nums:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} divisible by both 3 & 5")
    elif num % 5 == 0:
        print(f"{num} divisible by 5")
    elif num % 3 == 0:
        print(f"{num} divisible by 3")