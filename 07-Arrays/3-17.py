tuple = (50,20,40,50,30,50)
count = 0
for i in tuple:
    if i == 50:
        count += 1
        
print('Tuple',*tuple)
print('Value:', 50)
print('Number of occurrences:',count)