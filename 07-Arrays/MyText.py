def words_num(text):
    words = text.split()
    return len(words)

def ordered_words(text):
    words = text.split()
    return sorted(words, key = len, reverse = True)

def alphabetically_ordered(text):
    words = text.split()
    return sorted(words)
