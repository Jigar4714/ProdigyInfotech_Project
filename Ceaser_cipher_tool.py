def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char

    return result


# User input
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Perform encryption or decryption
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")