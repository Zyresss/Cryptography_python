from alphabet.alphabet import AlphabetMap, ReverseAlphabetMap

class vigenere:
    def __init__(self, key: str):
        self.key = key.upper()

    def encrypt(self, plaintext):
        ciphertext = ""
        plaintext = plaintext.replace(" ", "").upper()
        key_length = len(self.key)
        for i in range(len(plaintext)):
            char = plaintext[i]
            key_char = self.key[i % key_length]
            enc_char = (AlphabetMap[char] + AlphabetMap[key_char]) % 26
            ciphertext += ReverseAlphabetMap[enc_char]
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        ciphertext = ciphertext.replace(" ", "").upper()
        key_length = len(self.key)
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            key_char = self.key[i % key_length]
            dec_char = (AlphabetMap[char] - AlphabetMap[key_char]) % 26
            plaintext += ReverseAlphabetMap[dec_char]
        return plaintext

        




    # def encrypt(self, plaintext):
    #     ciphertext = ""
    #     plaintext = plaintext.replace(" ", "")
    #     key_length = len(self.key)
    #     for i in range(len(plaintext)):
    #         char = plaintext[i].upper()
    #         key_char = self.key[i % key_length].upper()
    #         if char.isalpha():
    #             x = AlphabetMap[char]
    #             k = AlphabetMap[key_char]
    #             y = (x + k) % 26
    #             ciphertext += ReverseAlphabetMap[y]
    #         else:
    #             ciphertext += char
    #     return ciphertext
    
    # def decrypt(self, ciphertext):
    #     plaintext = ""
    #     ciphertext = ciphertext.replace(" ", "")
    #     key_length = len(self.key)
    #     for i in range(len(ciphertext)):
    #         char = ciphertext[i].upper()
    #         key_char = self.key[i % key_length].upper()
    #         if char.isalpha():
    #             y = AlphabetMap[char]
    #             k = AlphabetMap[key_char]
    #             x = (y - k) % 26
    #             plaintext += ReverseAlphabetMap[x]
    #         else:
    #             plaintext += char
    #     return plaintext
    


