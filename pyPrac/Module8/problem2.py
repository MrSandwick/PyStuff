# Problem2_CompareTo10.py
# Baatyrbek Turatov
# June 18, 2024
# Compares the sum of two numbers to 10

def compare_to_10():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    
    if total > 10:
        print("Sum is greater than 10")
    elif total < 10:
        print("Sum is less than 10")
    else:
        print("Sum is equal to 10")

compare_to_10()