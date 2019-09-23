import decrypt

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encode_key(password):
    password = password.encode()
    salt = b'salt_Mackenzie2019'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key


def encode_message(plaintext, key):
    f = Fernet(key)
    token = f.encrypt(plaintext.encode())

    with open('ciphertext.bin', 'wb') as cyphertext:  
        cyphertext.write(token)


