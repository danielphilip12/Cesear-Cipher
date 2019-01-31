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


# string = "Hello World I am Daniel"
# encrypted_string = encrypt(string, 7)
# decrypted_string = decrypt(encrypted_string, 7)
# print(string)
# print(encrypted_string)
# print(decrypted_string)

