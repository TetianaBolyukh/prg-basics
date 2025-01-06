import matplotlib.pyplot as plt
temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(map(str, temp.keys()))
temperatures = list(map(int,temp.values()))

plt.bar(cities,temperatures)
plt.title('Recorded temperatures')
plt.xlabel('Cities')
plt.ylabel('Temperatures')
plt.show()