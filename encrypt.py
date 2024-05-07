from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved successfully.")
    return key

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Key file not found. Please generate a key first.")
        exit()

def encrypt_file(file_path, key):
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        encrypted_file_path = os.path.splitext(file_path)[0] + ".mahmoud"
        if os.path.exists(encrypted_file_path):
            if input("Encrypted file already exists. Overwrite? (y/n): ").lower() != 'y':
                print("Encryption canceled.")
                return
        with open(encrypted_file_path, "wb") as file:
            file.write(encrypted_data)
        print("File encrypted successfully.")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_file(file_path, key):
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        original_path = file_path.replace(".mahmoud", "")
        if os.path.exists(original_path):
            if input("File will be overwritten. Continue? (y/n): ").lower() != 'y':
                print("Decryption canceled.")
                return
        with open(original_path, "wb") as file:
            file.write(decrypted_data)
        print("File decrypted successfully.")
    except FileNotFoundError:
        print("Encrypted file not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")
    if choice.lower() == 'e':
        if input("Generate a new key? (y/n): ").lower() == 'y':
            key = generate_key()
        else:
            key = load_key()
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path, key)
    elif choice.lower() == 'd':
        key = load_key()
        file_path = input("Enter the path of the file to decrypt (.mahmoud): ")
        decrypt_file(file_path, key)
    else:
        print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
