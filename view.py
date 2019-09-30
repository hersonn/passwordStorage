import os
from tabulate import tabulate


# Print formated table
def showPasswordTable(decryptedMessage, stop):

    # Organize Decrypted Message into a Table
    table = createTable(decryptedMessage)

    # Show Table
    print("\n" + table + "\n")
    if stop == True:
        os.system("read -r key")


# Aux for showPasswordTable() to format decryptedMessage into Tabulate input format
def createTable(decryptedMessage):
    apps = []
    users = []
    pws = []
    notes = []

    # Split in decryptedMessage in lines
    nlines = decryptedMessage.split("[nl]")

    # Insert each line in a List, cleaning empty entries
    lines = list(filter(None, nlines))

    # Split each Line and concat each column in a new list
    for line in lines:
        column = line.split("[nc]")
        apps = apps + [column[0]]
        users = users + [column[1]]
        pws = pws + [column[2]]
        notes = notes + [column[3]]

    # Create a dict using Tabulate
    plain_text = tabulate(
        {
            "App": apps,
            "User": users,
            "Password": pws,
            "Note": notes
        },
        headers="keys")

    return plain_text


# Search for keyword in decryptedMessage, return lines OR ""
def search(decryptedMessage, keyword):

    # Split decryptedMessage
    lines = decryptedMessage.split("[nl]")

    # Result
    result = ""

    # Search for Keyword in each line
    for line in lines:
        if keyword in line:
            result = result + "[nl]" + line

    # Return lines in case
    return result


# Print Master Key
def master_key(key):
    print("\n" + key.decode("utf-8") + "\n")
    os.system("read -r -p 'Press any key to continue...' key")


# Print Cipher Text
def ciphertext():
    f = open("ciphertext.bin","r+")
    print("\n" + f.read() + "\n")
    f.close()
    os.system("read -r -p 'Press any key to continue...' key")
