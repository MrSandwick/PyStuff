# Problem2_CheckRange.py
# Baatyrbek Turatov
# June 18, 2024
# Problem 2: Check if a number is in the range 1 to 10.
def checkRange(n):
    if n in range(1, 11):
        print(n, "is in the range")
    else:
        print(n, "is not in the range")

checkRange(5)
checkRange(11)