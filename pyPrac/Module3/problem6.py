# Baatyrbek Turatov
# 4/26/2025
# Askes user for input and convert it to Celsius

key = input("Hello, select temperature measurement: Fahrenheit/Celsius.\nEnter F/C\n").lower()

if key == 'f':
    try:
        userDeg = float(input("Please, enter your room temperature:\n"))
        userDeg = (userDeg - 32) * 5 / 9
        print(f"Your room is {userDeg:.2f} degrees Celsius")
    except ValueError:
        print("Use only numbers.")
elif key == 'c':
    try:
        userDeg = float(input("Please, enter your room temperature:\n"))
        userDeg = (userDeg * 9 / 5) + 32
        print(f"Your room is {userDeg:.2f} degrees Fahrenheit")
    except ValueError:
        print("Use only numbers.")
else:
    print("Try again.")