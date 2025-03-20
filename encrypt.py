# Implement a basic Caesar cipher to encrypt and decrypt
#  messages

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    for char in text:
        if char.isalpha():  # Encrypt/decrypt only letters
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += new_char
        else:
            result += char  # Keep spaces and symbols unchanged

    return result

# Get user input
message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

# Encrypt or Decrypt
if mode == "encrypt":
    encrypted_message = caesar_cipher(message, shift, "encrypt")
    print(f"Encrypted Message: {encrypted_message}")
elif mode == "decrypt":
    decrypted_message = caesar_cipher(message, shift, "decrypt")
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
