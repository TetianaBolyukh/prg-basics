import re
def count_vowels(text):
    pattern = r'[AEIOUaeiou]'
    vowels = re.findall(pattern,text)
    print('The number of vowels is:',len(vowels))

text = input('Enter the text: ')
count_vowels(text)