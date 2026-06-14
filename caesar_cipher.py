def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char

    return result

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt: ").lower()

print("Result:", caesar_cipher(message, shift, mode))
