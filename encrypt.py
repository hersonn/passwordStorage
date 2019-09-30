import decrypt

import base64
import os
import uuid
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encode_key(password):
    # Password in bytes
    password = password.encode()

    # Salt = Mac Adress in bytes
    salt = hex(uuid.getnode()).encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    #print("Key: " + str(key))
    #os.system("read -r -p 'Press any key to continue...' key")

    return key


def encode_message(plaintext, key):
    f = Fernet(key)
    token = f.encrypt(plaintext.encode())

    with open('ciphertext.bin', 'wb') as cyphertext:
        cyphertext.write(token)
