from cryptography.fernet import Fernet


def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(plaintext)

    with open(output_file, 'wb') as file:
        file.write(ciphertext)


def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        ciphertext = file.read()

    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(ciphertext)

    with open(output_file, 'wb') as file:
        file.write(plaintext)
