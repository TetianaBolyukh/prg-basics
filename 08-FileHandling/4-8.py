import re
def four_char_extention(filename):
    try:  
        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                if re.match(r'[a-zA-Z0-9]{4}',line):
                    print(line)
    except FileNotFoundError:
        print(f'The file {filename} is not found')