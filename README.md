# File Encryption Script
This script encrypts all files in the current directory except for the script itself (main.py) and the key file (key.key). It uses the cryptography library to generate a key and encrypt the files.

# Prerequisites
Make sure you have Python installed. You can download it from python.org.

You also need to install the cryptography library. You can install it using pip:
pip install cryptography

How to Use
Save the provided Python script as main.py in the directory containing the files you want to encrypt.

Run the script:
python main.py

This script will:

Generate an encryption key and save it to a file named key.key.
Encrypt all files in the directory except for main.py and key.key.
Check the encrypted files:
After running the script, all targeted files will be encrypted. You can see the list of encrypted files printed by the script.

