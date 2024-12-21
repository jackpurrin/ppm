from cryptography.fernet import Fernet

def write_key():
    keyName = input("What do you want to name the key? ")
    key = Fernet.generate_key()
    with open(keyName + ".key", "wb") as key_file:
        key_file.write(key)
    print("Done!")
    menu()

def load_key():
    keyName = input("What is the key's name? ")
    return open(keyName, "rb").read()
    print("Done!")
    menu()

def encrypt(filename, key):
    file = open(key, "r")
    content = file.read()
    key = content
    file.close()
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print("Done!")
    menu()

def decrypt(filename, key):
    file = open(key, "r")
    content = file.read()
    key = content
    file.close()
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def menu():
    print("1). Generate a key")
    print("2). Read a key")
    print("3). Encrypt a file")
    print("4). Decrypt a file.")
    print("5). Exit")
    task = input("What do you want to do? ")

    if task == "1" :
        keyName = input("What do you want to name the key? ")
        write_key()
    if task == "2" :
        print(load_key())
    if task == "3" :
        encrypt(input("What file do you want to encrypt? "), input("What is the name of the key to encrypt the file? "))
    if task == "4" :
        decrypt(input("What file do you want to decrypt? "), input("What is the key used to encrypt the file? "))

menu()