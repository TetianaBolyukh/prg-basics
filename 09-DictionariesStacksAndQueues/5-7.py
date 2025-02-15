hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    return ", ".join([hotel["name"] for hotel in hotels])

def avg_price(hotels):
    total_price = sum(hotel["price"] for hotel in hotels)
    return round(total_price / len(hotels))

avg_price_Krakow = avg_price(hotels_in_Krakow)
avg_price_Sopot = avg_price(hotels_in_Sopot)

cheaper = []
if avg_price_Krakow<avg_price_Sopot:
    cheaper.append("Krakow")
elif avg_price_Sopot<avg_price_Krakow:
    cheaper.append("Sopot")

print(f'''
Hotels in Krakow: {hotel_list(hotels_in_Krakow)}
Average hotel price in Krakow: {avg_price_Krakow}
Hotels in Sopot: {hotel_list(hotels_in_Sopot)}
Average hotel price in Sopot: {avg_price_Sopot}
Cheaper hotels in: {', '.join(cheaper)}
''')