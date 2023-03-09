class Cipher:

  def __init__(self):
    self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

  def encrypt_message(self, message):
    message = message.upper()
    encrypted_message = ""
    for letter in message.upper():
      if letter in self.alphabet:
        encrypted_message += self._encrypt_letter(letter)
      else:
        encrypted_message += letter
    return encrypted_message

  def decrypt_message(self, message):
    message = message.upper()
    decrypted_message = ""
    for letter in message.upper():
      if letter in self.alphabet:
        decrypted_message += self._decrypt_letter(letter)
      else:
        decrypted_message += letter
    return decrypted_message

  def _encrypt_letter(self, letter):
    location = self.alphabet.index(letter)
    encoded_location = 25 - location
    return self.alphabet[encoded_location]

  def _decrypt_letter(self, letter):
    location = self.alphabet.index(letter)
    decoded_location = 25 - location
    return self.alphabet[decoded_location]
