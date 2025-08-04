
from hachicrypt import encrypt, decrypt

def main():
    message = "Welcome to Hachicrypt!"
    key = "mysecret"

    encrypted = encrypt(message, key)
    print(f"Encrypted message: {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()