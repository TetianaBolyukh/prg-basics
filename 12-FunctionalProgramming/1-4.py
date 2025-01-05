ms1 = 10
ms2 = 35

kmh = lambda x: int(x*3.6)

result1 = kmh(ms1)
result2 = kmh(ms2)

print(f'{ms1}m/s is {result1}km/h')
print(f'{ms2}m/s is {result2}km/h')