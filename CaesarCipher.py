import string

def crack_caesar(crypt_string, shift_amount):
    lower_alphabet = list(string.ascii_lowercase*2) # Make it possible to wrap around when going > 26 letters
    upper_alphabet = list(string.ascii_uppercase*2)
    cracked_string = ""

    for char in crypt_string:
        if char in lower_alphabet:
            found_index = lower_alphabet.index(char)
            cracked_string += lower_alphabet[found_index+shift_amount]
        elif char in upper_alphabet:
            found_index = upper_alphabet.index(char)
            cracked_string += upper_alphabet[found_index+shift_amount]
        else:
            cracked_string += char
    print(cracked_string)

while True:
    print("Enter a string to encrypt or decrypt")
    input_string = input()
    print("Enter the character shift (Must be a positive or negative integer)")
    shift_amount = input()
    crack_caesar(input_string, int(shift_amount))