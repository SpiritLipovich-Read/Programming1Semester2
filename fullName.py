pig = "ay"

string = input('Pig Latin-ifier')
word = string.lower()
first = word[0]
new_word = word[1:] + first + pig

print('Pig Latin-ified! ' + new_word)
