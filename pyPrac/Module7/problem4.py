# Problem4_Unique.py
# Baatyrbek Turatov
# June 18, 2024
# Problem 4: Return list with unique elements using append.
def uniqueElements(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

original_list = [1, 3, 3, 3, 6, 2, 3, 5]
print("Unique elements:", uniqueElements(original_list))