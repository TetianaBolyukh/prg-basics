###
# Write a program that allows you to convert time in 24-hour 
# format 3 to 12-hour format. The time in 24-hour 
# format (hh:mm) is read from the keyboard
#
time_24 = (input("Enter time (24-hour format): "))
hours_24= int(time_24[:2])
minutes = time_24[3:]
if hours_24 == 0:
    hours_12 = 12
    period = "am"
elif hours_24 == 12:
    hours_12 = 12
    period = "pm"
elif hours_24 > 12:
    hours_12 = hours_24 - 12
    period = "pm"
elif hours_24 < 12:
    hours_12 = hours_24
    period = "am"
print(f"Time in 12-hour format: {hours_12}:{minutes}{period}")