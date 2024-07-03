def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Welcome to Secret Agent Cipher!")
    print("-------------------------------")
    while True:
        print("\nMenu:")
        print("1. Encrypt a secret message")
        print("2. Decrypt a coded message")
        print("3. Exit")
        choice = input("Enter your mission (1/2/3): ").strip()

        if choice == '1':
            text = input("Enter the secret message to encrypt: ").strip()
            while True:
                try:
                    shift = int(input("Enter the encryption shift value (0-25): ").strip())
                    if 0 <= shift <= 25:
                        encrypted_message = caesar_cipher_encrypt(text, shift)
                        print(f"\nEncrypted secret message: {encrypted_message}\n")
                        break
                    else:
                        print("Shift value must be between 0 and 25.")
                except ValueError:
                    print("Invalid input. Shift value must be an integer.")
        
        elif choice == '2':
            text = input("Enter the coded message to decrypt: ").strip()
            while True:
                try:
                    shift = int(input("Enter the decryption shift value (0-25): ").strip())
                    if 0 <= shift <= 25:
                        decrypted_message = caesar_cipher_decrypt(text, shift)
                        print(f"\nDecrypted coded message: {decrypted_message}\n")
                        break
                    else:
                        print("Shift value must be between 0 and 25.")
                except ValueError:
                    print("Invalid input. Shift value must be an integer.")
        
        elif choice == '3':
            print("\nExiting the Secret Agent Cipher. Mission accomplished!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
