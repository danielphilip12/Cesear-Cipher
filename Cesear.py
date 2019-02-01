alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(string, key):
    string = string.lower()
    new_string = ""
    for i in string:
        if i in alphabet:
            x = alphabet.index(i)
            new_letter_loc = (x + key) % 26
            new_string += alphabet[new_letter_loc]
        else:
            new_string += i

    return new_string


def decrypt(string, key):
    string = string.lower()
    new_string = ""
    for i in string:
        if i in alphabet:
            x = alphabet.index(i)
            new_letter_loc = (x - key) % 26
            new_string += alphabet[new_letter_loc]
        else:
            new_string += i

    return new_string


x = input("Enter a string: ")
key = int(input("Enter a number between 1-26: "))
new_x = encrypt(x, key)
print(x)
print(new_x)
