alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 5
letter = input("What letter: ")
#A comment for testing
x = alphabet.index(letter)
new_letter_loc = (x + key) % 26
print(alphabet[new_letter_loc])
