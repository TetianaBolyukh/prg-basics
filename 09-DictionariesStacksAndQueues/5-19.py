import json

with open('reservations.json','r',encoding="utf-8") as file:
    data = json.load(file)

if 'reservations' in data:
    data = data["reservations"]

def rooms_number():
    return len(data)

def paid_reservations():
    paid = 0
    for reservation in data:
        if reservation['paid']:
            paid += 1
    return paid

def unpaid_reservations():
    unpaid = 0
    for reservation in data:
        if not reservation['paid']:
            unpaid += 1
    return unpaid

def value_of_paid():
    total_value = 0
    for reservation in data:
        if reservation['paid']:
            total_value += reservation["price_per_night"] * reservation['nights']
    return total_value

def value_of_unpaid():
    total_value = 0
    for reservation in data:
        if not reservation['paid']:
            total_value += reservation["price_per_night"]
    return total_value

print(rooms_number())
print(paid_reservations())
print(unpaid_reservations())
print(value_of_paid())
print(value_of_unpaid())