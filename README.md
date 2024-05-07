This Python script uses the `cryptography.fernet` library to encrypt and decrypt files securely. Here’s a breakdown of its components and functionalities:

### Libraries Used
- **cryptography.fernet**: Provides high-level cryptographic recipes and primitives. It's reliable for encrypting and decrypting data.
- **os**: Standard library in Python used to interact with the operating system, including path manipulations and file checks.

### Functions

1. **generate_key()**:
   - Generates a symmetric encryption key using Fernet.
   - Saves this key to a file named `secret.key`.
   - Returns the generated key.

2. **load_key()**:
   - Tries to open and read the `secret.key` file to load the encryption key.
   - If the file is not found, it prints an error message and exits the program, prompting the user to generate a key first.

3. **encrypt_file(file_path, key)**:
   - Takes a file path and the encryption key as input.
   - Encrypts the file using the provided Fernet key.
   - If an encrypted version of the file already exists, it asks the user if they want to overwrite it.
   - Saves the encrypted data to a new file with the same name but a custom extension `.mahmoud`.
   - Handles errors like file not found or other exceptions during the encryption process.

4. **decrypt_file(file_path, key)**:
   - Decrypts a file specified by `file_path` using the provided Fernet key.
   - Checks if the original file will be overwritten and asks the user for confirmation.
   - Saves the decrypted data back to its original format.
   - Handles file not found and other exceptions during the decryption process.

### Main Execution Flow
- The script prompts the user to choose between encrypting or decrypting a file.
- Based on the user's choice, it either:
  - Asks for a new key to be generated or to load an existing one, then proceeds to encrypt a specified file.
  - Loads an existing key and proceeds to decrypt a specified file.

- **Dependencies**: Make sure to note that `cryptography` library is required. It can be installed using `pip install cryptography`.
- **Security Notice**: Highlight the importance of securely managing the `secret.key` file, as it is crucial for decryption.
- **Usage Instructions**: Provide a simple example or step-by-step instructions on how to use the script to encrypt and decrypt files.
- **Error Handling**: Discuss the error handling done in the script, particularly around file existence checks and exception management during encryption and decryption processes.
- **File Extension**: The `.mahmoud` extension is used for encrypted files, which is a custom choice and can be changed based on user preference.
