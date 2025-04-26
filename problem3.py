# Baatyrbek Turatov
# 4/26/2025
# Askes user for input and checks if user is me or Akshay then give greeting according to user

print("Hi, please enter your name:")
userName = input().capitalize()
if userName == "Baatyrbek":
    print("Greetings, my lord!")
elif userName == "Akshay" or userName =="Mestry":
    print("Hello, professor Akshay!")
else:
    print(f"Hi, the most ordinary user, {userName}!")

