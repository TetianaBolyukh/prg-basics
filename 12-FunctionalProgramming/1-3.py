def ms_to_kmh(ms):
    kmh = int(ms*3600/1000)
    return kmh

ms1 = 10
ms2 = 35
kmh1 = ms_to_kmh(ms1)
kmh2 = ms_to_kmh(ms2)

print(f'{ms1}m/s is {kmh1}km/h')
print(f'{ms2}m/s is {kmh2}km/h')