# Problem4_LeapYear.py
# Baatyrbek Turatov
# June 18, 2024
# Determines if a year is a leap year

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0

# Test cases
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2024))  # True