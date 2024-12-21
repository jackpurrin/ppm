from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('encr.key', 'wb') as encr:
    encr.write(key)

with open('encr.key', 'rb') as encr:
    key = encr.read()

print('DEBUG ONLY!!!! REMOVE IN PROD!! ', key)

f = Fernet(key)

with open('grades.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_grades.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)