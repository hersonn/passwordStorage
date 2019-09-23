import encrypt
import decrypt
import view

import os

# Aux - Input data in a correct format
def take_data():
    app  = input("App: ")
    user = input("User: ")
    pw   = input("Password: ")
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
        view.showPasswordTable(result)
    else:    
        print("Any keyword found!")
        os.system("read -r key")


# Input a new registry line
def input_password(decryptedMessage, key):
    print("\nInput a new registry: ")
    
    newEntry = take_data()
    plaintext =  decryptedMessage + newEntry

    encrypt.encode_message(plaintext, key)


# Remove a registry line
def remove_password(decryptedMessage, key):


    result = view.search(decryptedMessage)
    print(result.find('[nl]'))

    if (result.find('[nl]') > -1): 
        print ("Contains given substring ") 
    else: 
        print ("Doesn't contains given substring") 
    os.system("read -r -p 'Press any key to continue...' key")


# Edit a registry line
def edit_password(decryptedMessage, key):

    os.system("read -r -p 'Press any key to continue...' key")
