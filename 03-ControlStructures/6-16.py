total_washing_time = 0
jacket_time = 40
underwear_time = 70
shoes_time = 20
extra_rinse_time = 15
extra_spin_time = 9

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')
if program == "j":
    print('washing_product = "jacket"')
    total_washing_time += jacket_time
elif program == "u":
    print('washing_product = "underwear"')
    total_washing_time += underwear_time
elif program == "s":
    print('washing_product = "shoes"')
    total_washing_time += shoes_time

if extra_rinse == "y":
    print("rinse = True")
    total_washing_time += extra_rinse_time
else:
    print("rinse = False")

if extra_spin == "y":
    print("spin = True")
    total_washing_time += extra_spin_time
else:
    print("spin= False")

print(f"Total washing time: {total_washing_time}")
