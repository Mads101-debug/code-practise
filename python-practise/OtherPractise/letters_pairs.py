#code I wrote myself
from string import ascii_lowercase

alphabet = ascii_lowercase

individual_letter = alphabet

letters = ([x for x in ascii_lowercase])

index = -1
while index != 25:
    index += 1
    for i in individual_letter:
        combo = (letters[index] + i)
        print(combo)


#code someone else wrote, makes soooo much sense, easier, simple, basic
""" import string

temp = string.ascii_lowercase

for i in temp:
    for j in temp:
        print(i+j) """


#another simple af code
""" from string import ascii_lowercase as lowercase_letters

for first_letter in lowercase_letters:
    for second_letter in lowercase_letters:
        print(first_letter + second_letter) """


#code i wrote all combos of letters printed expect same letters 'aa', 'bb'
""" alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_pairs = []
for first_letter in alphabet:
    for second_letter in alphabet:
        letter_pair = first_letter + second_letter
        letter_pairs.append(letter_pair)
            
same_letters = []                                                
for letter in alphabet:
        same_letter = letter + letter
        same_letters.append(same_letter)

for i in same_letters:
    letter_pairs.remove(i)
    
letter_pairs.sort()
for j in letter_pairs:
    print(j) """