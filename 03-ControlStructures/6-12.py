###
# Calculates the amount to be paid
#
product_number = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))
if product_number >= 2:
    amount_pay = (product_price-(product_price*0.25))*product_number
    print(f"Amount to pay: {amount_pay}")
else:
    amount_pay = product_number*product_price
    print(f"No discount for you, amount to pay: {amount_pay}")