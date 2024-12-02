import json

product = {}

# read product data from keyboard
product['name'] = input('Enter name: ')
product['price'] = input('Enter price: ')
product['paid'] = input('Is it paid? (y/n) ')

# save product data to json file
if product['paid'] == 'y':
    product['paid'] = True
else:
    product['paid'] = False

file_name = 'product.json'

with open(file_name, 'w') as file:
    json.dump(product, file, indent=4)

print('Data was written to', file)