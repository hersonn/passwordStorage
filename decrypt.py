import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def decode_message(key):
    with open('ciphertext.bin', 'rb') as file_object:
        for line in file_object:
            encryptedpwd = line

    f = Fernet(key)
    uncipher_text = (f.decrypt(encryptedpwd))
    plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8")

    return plain_text_encryptedpassword
