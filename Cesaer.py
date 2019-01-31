alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(string, key):
    string = string.lower()
    new_string = ""
    for i in string:
        if(i in alphabet):
            x = alphabet.index(i)
            new_letter_loc = (x + key) % 26
            new_string += alphabet[new_letter_loc]
        else:
            new_string += i

    return new_string

x = "Hello World"
encrypted_x = encrypt(x, 7)
print(x)
print(encrypted_x)