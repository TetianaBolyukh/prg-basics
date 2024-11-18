arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest_word = ''
for word in arr:
    if len(word) > len(longest_word):
        longest_word = word
print('Names', *arr)
print('Longest name:', longest_word)
