###
# Checks whether the number entered from the keyboard consists of exactly 13 characters
# and when the article number is correct, print a message when the product
# was manufactured in Poland
#
number = (input("Enter EAN-13 article number: ")) 
if len(number) == 13 and number.isdigit():
    print(f"Article number is correct")
    if number.startswith("590"):
        print("Article sanufactured in Poland")