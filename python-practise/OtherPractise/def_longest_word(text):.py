def longest_word(text):
    text = text.split()
    long_word = max(text, key = len)
    return long_word
