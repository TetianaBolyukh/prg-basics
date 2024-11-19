with open('email.txt','r') as file:
    content = file.read()

for line in content:
    if '' in line:
        print()