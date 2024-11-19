with open('countries.txt','r') as file:
    content = file.read()

i=1
for line in content:
    print(f'{i}. {line}')
    i += 1