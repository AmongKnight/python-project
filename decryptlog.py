from cryptography.fernet import Fernet

logfile = 'keyloggs.txt'
keyfile = 'encryption_key.key'

# Load the encryption key
def load_key():
    with open(keyfile, 'rb') as key_in:
        return key_in.read()

# Decrypt data
def decrypt(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

# Load the encryption key
key = load_key()

# Read and decrypt the log file
with open(logfile, 'rb') as f:
    encrypted_lines = f.readlines()

decrypted_words = [decrypt(line.strip(), key) for line in encrypted_lines]

for word in decrypted_words:
    print(word)
