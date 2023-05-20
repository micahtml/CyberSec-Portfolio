from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    return key


# Example usage:
key = generate_key()
