# Baatyrbek Turatov
# 4/26/2025
# Askes user for starting day and lenght of stay to calculate day of return + hashmap to indentify the `corresponding` day of return

days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

start_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))
stay_length = int(input("Enter the length of your stay (in nights): "))

# Calculate the return day number
return_day = (start_day + stay_length) % 7
print(f"You will return on day number {return_day}, which is a {days[return_day]}.")