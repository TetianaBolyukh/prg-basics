# Displays the first five lines from the it_company.csv file and then prints 
# 'Press Enter key...' in the next line and waits for the Enter key to be pressed
with open('it_company.csv', 'r') as file:
    while True:
        for line in range(5):
            printed_line = file.readline()
            if not printed_line:
                print('File lines ended')
            print(printed_line.strip())

        input('Press enter key...')
