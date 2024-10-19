###
# A computer program analyses the price of a product in an online store
# 
current_price = 140
previous_price = 200
print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")
decrease = 100-(current_price*100/previous_price)
if decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {decrease} %")