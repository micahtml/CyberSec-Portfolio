import key_management
import encryption
import user_interface

# Key generation and storage
key = key_management.generate_key()
key_management.save_key(key, 'keyfile.txt')

# Key loading
key = key_management.load_key('keyfile.txt')

# Encryption and decryption
encryption.encrypt_file(key, 'plaintext.txt', 'ciphertext.txt')
encryption.decrypt_file(key, 'ciphertext.txt', 'decrypted.txt')

# User interface
user_interface.start_gui()
