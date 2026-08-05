from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def getpassword():
    return input("Enter Password: ")


def decryption(input_file, output_file, password):

    try:
        with open(input_file, "rb") as inputFile:

            # Read salt
            salt = inputFile.read(16)
            if len(salt) != 16:
                raise ValueError("Invalid encrypted file (missing salt).")

            # Read IV
            iv = inputFile.read(16)
            if len(iv) != 16:
                raise ValueError("Invalid encrypted file (missing IV).")

            # Generate key
            key = PBKDF2(
                password.encode("utf-8"),
                salt,
                dkLen=32,
                count=1000000
            )

            cipher = AES.new(key, AES.MODE_CBC, iv)

            # Read ciphertext
            ciphertext = inputFile.read()

        if len(ciphertext) == 0:
            raise ValueError("Encrypted data missing.")

        if len(ciphertext) % AES.block_size != 0:
            raise ValueError("Encrypted file is corrupted.")

        # Decrypt
        plaintext = cipher.decrypt(ciphertext)

        # Remove PKCS#7 padding
        plaintext = unpad(plaintext, AES.block_size)

        # Save plaintext
        with open(output_file, "wb") as outputFile:
            outputFile.write(plaintext)

        print("Decryption successful!")

    except FileNotFoundError:
        print("Encrypted file not found.")

    except ValueError as e:
        print(f"Decryption Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


def main():

    choice = input("Enter 'd' for decryption: ").lower()

    if choice != "d":
        print("Invalid choice.")
        return

    password = getpassword()

    inputFile = "output_test_encyrpt.bin"
    outputFile = "input_test_decrypted.txt"

    decryption(inputFile, outputFile, password)


if __name__ == "__main__":
    main()