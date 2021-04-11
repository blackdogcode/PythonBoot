alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt_message(message, shift_count):
    encrypted_message = []
    for char in message:
        shifted_index = (alphabet.index(char)+shift_count) % len(alphabet)
        encrypted_message.append(alphabet[shifted_index])

    return "".join(encrypted_message)


if __name__ == "__main__":
    input_message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    print(f'Original Message: {input_message}')
    cipher_message = encrypt_message(message=input_message, shift_count=shift)
    print(f'Encrypted Message: {cipher_message}')
