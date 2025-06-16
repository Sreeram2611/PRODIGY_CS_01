def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Sreeram's Caesar Cipher Encryption and Decryption Tool")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please type 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
