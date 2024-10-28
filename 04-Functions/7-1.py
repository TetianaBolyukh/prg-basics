###
# Define a function month(n) that returns a month name based 
# on the month number (values from 1 to 12). Then, write a program 
# to print the name of the month 7. Import the module with the created function
def month():
    if number == 1:
        month = 'January'
    if number == 2:
        month = 'February'
    if number == 3:
        month = 'March'
    if number == 4:
        month = 'April'
    if number == 5:
        month = 'May'
    if number == 6:
        month = 'June'
    if number == 7:
        month = 'July'
    if number == 8:
        month = 'August'
    if number == 9:
        month = 'Sepmtember'
    if number == 10:
        month = 'October'
    if number == 11:
        month = 'November'
    if number == 12:
        month = 'December'
    return month

number = int(input('Enter month number: '))
print(f'The name of month {number} is {month()}') 