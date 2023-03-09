from cipher import Cipher


class CaesarCipher(Cipher):

  def __init__(self, shift):
    super().__init__()
    if isinstance(shift, int) and shift in range(0, 26):
      self.shift = shift
    else:
      raise ValueError("Shift value must be an integer between 0 and 25.")

  def _encrypt_letter(self, letter):
    location = self.alphabet.index(letter)
    encoded_location = (location + self.shift) % 26
    return self.alphabet[encoded_location]

  def _decrypt_letter(self, letter):
    location = self.alphabet.index(letter)
    decoded_location = (location - self.shift) % 26
    return self.alphabet[decoded_location]
