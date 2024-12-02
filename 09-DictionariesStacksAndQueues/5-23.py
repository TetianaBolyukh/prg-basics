import json
 
with open('euro.json', 'r') as file:
    data = json.load(file)

# Print the header
print("Date            Buying Rate     Selling Rate")
print("============================================")

for rate in data['rates']:
    date = rate['effectiveDate']
    buying_rate = rate['mid']
    selling_rate = rate['mid']
    print(f"{date}      {buying_rate:<10}      {selling_rate:<10}")
