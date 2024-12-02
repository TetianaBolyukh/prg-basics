translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
word = input('Enter a word to translate: ')
if word in translations:
        print(f'{word} is {translations[word]}')
if word not in translations:
    print('The translation is unavailable')