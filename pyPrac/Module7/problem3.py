# Problem3_MultiplyList.py
# Baatyrbek Turatov
# June 18, 2024
# Problem 3: Multiply all numbers in a list.
def multiplyList(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [5, 2, 7, -1]
print("Product of list:", multiplyList(numbers))