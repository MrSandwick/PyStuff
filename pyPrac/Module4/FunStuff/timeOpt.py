#Optimized code

while True:
    try:
        currentTime = int(input("What is the current time (in hours 0–23)?\n"))
        if 0 <= currentTime <= 23:
            print(f"OK, the time is {currentTime}:00")
            break  # Exit the loop when valid
        else:
            print("Please enter a number between 0 and 23.")
    except ValueError:
        print("That's not a valid number. Please enter an integer.")
waitTime = int(input("How many hours do you want to wait?\n"))
finalTime =  currentTime + waitTime
print(f"Sum of waiting time with current or something: {finalTime}")