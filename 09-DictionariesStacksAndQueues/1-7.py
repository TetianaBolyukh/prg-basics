products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
for key,value in products.items():
    print(f'{key}: {value}')

sum = 0
for value in products.values():
    sum += int(value)
print('Sum is',sum)