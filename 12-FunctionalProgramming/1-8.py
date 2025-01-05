name = input('Name: ')
surname = input('Surname: ')


initials = lambda name,surname: name[0] + surname[0]
result = initials(name,surname)
print(result)