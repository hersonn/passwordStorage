import encrypt
import decrypt
import crud
import view

import os
from cryptography.fernet import Fernet

if __name__ == "__main__":
    # Input Password
    password = input("Master Key: ")

    # Encrypt Key
    key = encrypt.encode_key(password)

    # Menu loop
    option = ''
    while option != '9':

        os.system("clear")

        # Main Menu
        print("\nMenu:")
        print("1. Show Password Table")
        print("2. Search")
        print("3. Add Password")
        print("4. Edit Password")
        print("5. Remove Password")
        print("6. Master Key Hash")
        print("7. Ciphertext")
        print("9. Exit")
        print("0. Reset/First Use")

        option = input("Option: ")

        # 0. Reset/First Use
        if option == '0':
            reset = input("All your data will be lost! Are you sure? (y/n): ")

            if reset == 'y':
                crud.reset(key)
            else:
                print("Operation aborted!")
                os.system("read -r -p 'Press any key to continue...' key")

        else:
            # Decrypt Message with the Key
            decryptedMessage = decrypt.decode_message(key)

            # 1. Show Password Table
            if option == '1':
                view.showPasswordTable(decryptedMessage, True)

            # 2. Search
            elif option == '2':
                crud.read(decryptedMessage)

            # 3. Add Password
            elif option == '3':
                crud.input_password(decryptedMessage, key)

            # 4. Edit Password
            elif option == '4':
                crud.edit_password(decryptedMessage, key)

            # 5. Remove Password
            elif option == '5':
                crud.remove_password(decryptedMessage, key)
            
            # 6. Show Password Hash
            elif option == '6':
               view.master_key(key)
            
            # 7. Print ciphertext.bin
            elif option == '7':
               view.ciphertext()

            # 9. Exit
            elif option == '9':
                os.system('clear')

            # Invalid Option
            else:
                print("\nInvalid Option")
                os.system("read -r -p 'Press any key to continue...' key")
