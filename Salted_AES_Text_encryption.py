from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

def getpassword():

    password = input("Enter Password: ")

    return password

def encryption(input_file, output_file, password):

    #generate random 16 bit salt
    salt = get_random_bytes(16)

    key = PBKDF2(password.encode('utf-8'), salt, dkLen=32, count=1000000)

    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    try:
        with open(input_file, 'rb') as inputFile, open(output_file, 'wb') as outputFile:

            outputFile.write(salt)
            outputFile.write(iv)

            while True:

                chunk = inputFile.read(4096)

                if len(chunk) == 0:
                    break

                if len(chunk) < 4096:
                    chunk = pad(chunk,16)


                cipherText = cipher.encrypt(chunk)

                outputFile.write(cipherText)

    except FileNotFoundError:
        print("One or the other file does not exist!")

def main():

    choice = input("enter 'e' for encryption: ").lower()

    password = getpassword()

    if choice == 'e':

        inputFile = "input_test_encrypt.txt"
        outputFile = "output_test_encyrpt.bin"

        encryption(inputFile, outputFile, password)

        print(f"file {inputFile} has been encrpted to {outputFile}")

    else:
        print("Invalid choice! please enter either 'e' or exit. ")
        raise SystemExit(1)
        
if __name__ == '__main__':
    main()