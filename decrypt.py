import encrypt

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

def brute_force():
    f = open('dictionary.txt')
    
    line = f.readline()
    while line:
        try:
            forceKey = line.strip("\n")
            key = encrypt.encode_key(forceKey)
            print(forceKey + "\t\t" + key.decode("utf-8"))
            decode_message(key)
        except:
            line = f.readline()
        else:
            print("\n" + forceKey + "\t\t" + key.decode("utf-8"))
            print("Password found!")
            break
    f.close()
    os.system("read -r key")
    


       
