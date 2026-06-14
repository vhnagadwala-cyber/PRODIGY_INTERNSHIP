# Task 01 - Caesar Cipher (Encryption & Decryption)
# Prodigy InfoTech Cyber Security Internship
# Author: Veer Nagadwala
#
# The Caesar Cipher is one of the oldest and simplest encryption techniques.
# It works by shifting every letter in your message by a fixed number of positions.
#
# Example with shift = 3:
#   A → D,  B → E,  C → F ... Z → C
#
# So "HELLO" becomes "KHOOR" with a shift of 3.
# To decrypt, you just shift back in the other direction.
#
# Fun fact: Julius Caesar actually used this cipher to send secret messages
# to his generals — that's how it got its name!


def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            # Figure out if it's uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')

            # Shift the letter and wrap around using % 26
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            # Keep spaces, numbers, punctuation as they are
            result += char

    return result


def decrypt(message, shift):
    # Decrypting is just encrypting in the opposite direction
    return encrypt(message, -shift)


def main():
    print("\n======================================")
    print("   Caesar Cipher Tool")
    print("   Prodigy InfoTech | Task 01")
    print("======================================")
    print("\nThis tool encrypts and decrypts messages using the Caesar Cipher.")
    print("Just enter your message and a shift number (e.g. 3).\n")

    while True:
        print("What do you want to do?")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Exit")

        choice = input("\nEnter 1, 2, or 3: ").strip()

        if choice == "3":
            print("\nGoodbye! Remember - keep your messages secret! 🔐")
            break

        if choice not in ("1", "2"):
            print("Invalid option. Please enter 1, 2, or 3.\n")
            continue

        message = input("\nEnter your message: ")

        try:
            shift = int(input("Enter the shift value (e.g. 3): ").strip())
        except ValueError:
            print("Shift must be a number! Try again.\n")
            continue

        if choice == "1":
            output = encrypt(message, shift)
            print(f"\nOriginal  : {message}")
            print(f"Encrypted : {output}")
            print(f"(Shift used: {shift})")

        elif choice == "2":
            output = decrypt(message, shift)
            print(f"\nEncrypted : {message}")
            print(f"Decrypted : {output}")
            print(f"(Shift used: {shift})")

        print("\n" + "─" * 40 + "\n")


if __name__ == "__main__":
    main()
