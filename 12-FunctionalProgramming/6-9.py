temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
def pos_temp(values):
    return lambda values: values > 0

result = list(filter(pos_temp, temp))
print('Cities with positive temperatures: ',*result)