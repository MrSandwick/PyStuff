# Problem3_CheckFor5.py
# Baatyrbek Turatov
# June 18, 2024
# Checks if 5 exists in a given list

def check_for_5(lst):
    if 5 in lst:
        print("5 is in the list")
    else:
        print("5 is not in the list")

# Test cases
check_for_5([1, 2, 3, 4, 5])  # Should find 5
check_for_5([6, 7, 8])        # Should not find 5