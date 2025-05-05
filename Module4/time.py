currentTimeStr = input("What is the current time (in hours 0-23)?\n")
waitTimeStr = input("How many hours do you want to wait?\n")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(f"Sum of waiting time with current or something: {finalTimeInt}")

