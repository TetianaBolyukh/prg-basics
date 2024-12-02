provinces_dict = {}
letter_counts = {}
with open('province.csv', 'r') as province_file:
    next(province_file)
    for line in province_file:
        letter,name = line.split(',')
        provinces_dict[letter] = name
        letter_counts[name] = 0

with open('vehicle.txt','r') as vehicle_file:
    for registration_number in vehicle_file:
        first_letter = registration_number[0]
        if first_letter in provinces_dict:
            province_name = provinces_dict[first_letter]
            letter_counts[province_name] += 1

for province,count in letter_counts.items():
    print(f'{province}: {count}')