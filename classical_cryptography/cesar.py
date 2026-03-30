from alphabet.alphabet import AlphabetMap, ReverseAlphabetMap

class cesar:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, plaintext):
        ciphertext = ""
        plaintext = plaintext.replace(" ", "")
        for char in plaintext.upper():
            if (ord(char) + self.shift) > (ord('Z')):
                ciphertext += chr(ord(char) + self.shift - 26)
            else:
                ciphertext += chr(ord(char) + self.shift)
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        ciphertext = ciphertext.replace(" ", "")
        for char in ciphertext.upper():
            if ord(char) < (ord('A') + self.shift):
                plaintext += chr(ord(char) - self.shift + 26)
            else:
                plaintext += chr(ord(char) - self.shift)
        return plaintext
    
# class Cesar:
#     def __init__(self, shift):
#         self.shift = shift

#     def encrypt(self, plaintext):
#         ciphertext = ""
#         for char in plaintext:
#             if char.isalpha():
#                 char = char.upper()
#                 shifted_char = (AlphabetMap[char] + self.shift) % 26
#                 ciphertext += ReverseAlphabetMap[shifted_char]
#             else:
#                 ciphertext += char
#         return ciphertext

#     def decrypt(self, ciphertext):
#         plaintext = ""
#         for char in ciphertext:
#             if char.isalpha():
#                 char = char.upper()
#                 shifted_char = (AlphabetMap[char] - self.shift) % 26
#                 plaintext += ReverseAlphabetMap[shifted_char]
#             else:
#                 plaintext += char
#         return plaintext
