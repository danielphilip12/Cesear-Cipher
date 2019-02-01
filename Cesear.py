alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#This function encrypts a string. It works by
#taking each letter in the string and adding the key.
#This changes the letter
def encrypt(string, key):
    #string = string.lower()
    new_string = ""
    for i in string:
        if i in alphabet:
            x = alphabet.index(i)
            new_letter_loc = (x + key) % 26
            new_string += alphabet[new_letter_loc]
        elif i in alpha_alphabet:
            x = alpha_alphabet.index(i)
            new_letter_loc = (x + key) % 26
            new_string += alpha_alphabet[new_letter_loc]
        else:
            new_string += i

    return new_string

#This function decrypts a string. It works by
#taking each letter in the string and subtracting the key from it
#in order to get the original letter
def decrypt(string, key):
    #string = string.lower()
    new_string = ""
    for i in string:
        if i in alphabet:
            x = alphabet.index(i)
            new_letter_loc = (x - key) % 26
            new_string += alphabet[new_letter_loc]
        elif i in alpha_alphabet:
            x = alpha_alphabet.index(i)
            new_letter_loc = (x - key) % 26
            new_string += alpha_alphabet[new_letter_loc]
        else:
            new_string += i

    return new_string

