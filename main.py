from cryptography.fernet import Fernet

print("python passw0rd manager")
print("not a safe password manager to use for daily use")
print("use for testing only! no secrets!")

print("")
print("1.) Generate a key and encrypt a database")
print("2.) Make a database")

option = input("What do you want to do?")

if option == 1 :
    with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

print("done")

