import json
    
# Read the contents of the json file
try:
    with open('voting.json','r',encoding="utf-8") as file:
        voting_data = json.load(file)
except FileNotFoundError:
    voting_data = {}

# Vote for a person
while True:
    person_name = input('Name of the person you are voting for (type "e" to exit): ')
    if person_name.lower() == 'e':
        print('Your vote was saved!')
        break

    if person_name:
        if person_name in voting_data:
            voting_data[person_name] += 1
        else:
            voting_data[person_name] = 1
    else:
        print('Wrong input')
# Save voting data to json file
with open('voting.json','w') as file:
    json.dump(voting_data, file, ensure_ascii=False)

# Print data
for person,votes in voting_data.items():
    print(f'{person}:{votes}')