import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt_message(message, shift_count):
    encrypted_message = []
    for char in message:
        shifted_index = (alphabet.index(char) + shift_count) % len(alphabet)
        encrypted_message.append(alphabet[shifted_index])

    return "".join(encrypted_message)


def decrypt_message(message, shift_count):
    decrypted_message = []
    for char in message:
        shifted_index = (alphabet.index(char) + len(alphabet) - shift_count) % len(alphabet)
        decrypted_message.append(alphabet[shifted_index])

    return "".join(decrypted_message)


if __name__ == "__main__":
    print(art.logo)

    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        input_message = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))

        if direction == 'encode':
            cipher_message = encrypt_message(message=input_message, shift_count=shift)
            print(f'Encrypted Message: {cipher_message}')
        elif direction == 'decode':
            decipher_message = decrypt_message(message=input_message, shift_count=shift)
            print(f'Decrypted Message: {decipher_message}')
        else:
            print(f'Invalid Command {direction} is not neither "encode" nor "decode"')
