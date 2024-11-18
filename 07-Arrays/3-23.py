###
# A variable contains text:
# An apple a day keeps the doctor away

# Create a module MyText, containing:

# A function that returns the number of words in the text
# A function that returns an ordered array of words, from longest to shortest
# A function that returns an alphabetically ordered array of words
# Then, write a program, call the functions and print results. Sample result:
# 
# Text: An apple a day keeps the doctor away
# Number of words: 8
# Words from the longest: doctor,apple,…
# Words ordered alphabetically: a,An,apple,away,…
text = 'An apple a day keeps the doctor away'
print('Text:',text)
from MyText import words_num
from MyText import ordered_words
from MyText import alphabetically_ordered
print('Number of words:',words_num(text))
print('Words from the longest:',ordered_words(text))
print('Words ordered alphabetically:',alphabetically_ordered(text))