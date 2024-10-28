###
# Write a program that checks if the PIN code entered in the payment terminal is correct
#
pin = "0805"
count = 1
pin_enter = (input("Enter the PIN code: "))
while True:
    if count == 3:
        print("Sorry, your payment card has been blocked.")
        break
    elif len(pin_enter) != 4 or pin_enter != pin:
        print("Incorrect...")
        count += 1
        pin_enter = (input("Enter the PIN code: "))