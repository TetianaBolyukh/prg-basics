###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

num = 1
with open('it_company.csv', 'r') as file:
   for line in file:
      if job_title in line:
         print(f'{num}. {line}')
         num += 1