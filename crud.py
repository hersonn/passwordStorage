import encrypt
import decrypt
import view

import os

# Aux - Input data in a correct format
def take_data():
    app = input("App: ")
    user = input("User: ")
    pw = input("Password: ")
    note = input("Note: ")
    plaintext = app + "[nc]" + user + "[nc]" + pw + "[nc]" + note + "[nl]"

    return plaintext


# Reset full table
def reset(key):
    print("Please, inform your first entry: ")
    plaintext = take_data()

    # Encrypt Message with the Key
    encrypt.encode_message(plaintext, key)


# Search on decryptedMessage
def read(decryptedMessage):

    keyword = input("Search for: ")

    result = view.search(decryptedMessage, keyword)
    if result != "":
        view.showPasswordTable(result, True)
    else:
        print("\nAny keyword found!")
        os.system("read -r key")


# Input a new registry line
def input_password(decryptedMessage, key):
    print("\nInput a new registry: ")

    newEntry = take_data()
    plaintext = decryptedMessage + newEntry

    encrypt.encode_message(plaintext, key)


# Remove a registry line
def remove_password(decryptedMessage, key):

    keyword = input("Search for: ")
    result = view.search(decryptedMessage, keyword)
    
    view.showPasswordTable(result, False)
    op = input("\nAre you sure to delete this registry? (y/n): ")

    if op == "y":
        plaintext = decryptedMessage.replace(result, "")
        encrypt.encode_message(plaintext, key)
    else:
        print("Operation aborted!")
    
    os.system("read -r -p 'Press any key to continue...' key")

# Edit a registry line
#    os.system("read -r -p 'Press any key to continue...' key")
