# Eric Cuevas, Andrew Molina
# Assigned Mar 7, Due Mar 9
# A program that allows the user to encrypt or decrypt messages using different types of encryption methods.  Encrypted messages will read from the console and then written to a file called ‘message.txt’, and decrypted messages will be read from the ‘message.txt’ file then displayed to the console.

from cipher import Cipher
from caesar_cipher import CaesarCipher


def main():
  print("Secret Decoder Ring:\n1. Encrypt\n2. Decrypt\n3. Quit\n")

  while True:
    choice = input("Would you like to encrypt or decrypt a message?\n").lower()

    if choice in ["encrypt", "e", "1"]:
      encryption_method = input(
        "\nEnter encryption type:\n1. Atbash\n2. Caesar\n").lower()
      message = input("\nEnter message: ")

      if encryption_method in ["atbash", "1"]:
        cipher = Cipher()
        encrypted_message = cipher.encrypt_message(message)
      elif encryption_method in ["caesar", "2"]:
        shift = int(input("Enter the shift value (0-25): "))
        cipher = CaesarCipher(shift)
        encrypted_message = cipher.encrypt_message(message)
      else:
        print("Invalid encryption method.")
        return

      with open("message.txt", "w") as file:
        file.write(encrypted_message)
        print(f"\nEncrypted message: {encrypted_message}")
        print("Message written to message.txt.\n")

    elif choice in ["decrypt", "d", "2"]:
      decryption_method = input(
        "Enter decryption type:\n1. Atbash\n2. Caesar\n").lower()

      with open("message.txt", "r") as file:
        message = file.read()

      if decryption_method in ["atbash", "1"]:
        cipher = Cipher()
        decrypted_message = cipher.decrypt_message(message)
      elif decryption_method in ["caesar", "2"]:
        shift = int(input("Enter the shift value (0-25): "))
        cipher = CaesarCipher(shift)
        decrypted_message = cipher.decrypt_message(message)
      else:
        print("Invalid encryption method.")
        return
      print(f"Decrypted message: {decrypted_message}")

    else:
      print("Invalid choice.")
      continue


if __name__ == '__main__':
  main()
