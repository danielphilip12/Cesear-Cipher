alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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


# word = "Hello World"
# en = encrypt(word, 7)
# de = decrypt(en, 7)
# print(word)
# print(en)
# print(de)