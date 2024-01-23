import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(text, shift):
    encode_text = ""
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char) + shift
            if pos >= len(alphabet):
                pos -= len(alphabet)
            encode_text += alphabet[pos]
        else:
            encode_text += char
    return encode_text


def decryption(text, shift):
    decode_text = ""
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char) - shift
            if pos < 0:
                pos += len(alphabet)
            decode_text += alphabet[pos]
        else:
            decode_text += char
    return decode_text


print(art.logo)
print("Welcome to Caesar Cipher")

is_continue = True
while is_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message to encrypt\n")
        shift_num = int(input("How many shifts do you want to encrypt?\n"))
        encode_text = encryption(text, shift_num % len(alphabet))
        print(f"Encrypted text: {encode_text}")
    elif direction == "decode":
        text = input("Type your message to decrypt\n")
        shift_num = int(input("How many shifts do you want to decrypt?\n"))
        decode_text = decryption(text, shift_num % len(alphabet))
        print(f"Decrypted text: {decode_text}")
    else:
        print(f"Invalid Command")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        is_continue = False
        print("Goodbye")
