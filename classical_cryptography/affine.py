from alphabet.alphabet import AlphabetMap, ReverseAlphabetMap

class affine :
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def encrypt(self, plaintext):
        ciphertext = ""
        plaintext = plaintext.replace(" ", "")
        for char in plaintext.upper():
            if char.isalpha():
                x = AlphabetMap[char]
                y = (self.a * x + self.b) % 26
                ciphertext += ReverseAlphabetMap[y]
            else:
                ciphertext += char
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        ciphertext = ciphertext.replace(" ", "")
        for char in ciphertext.upper():
            if char.isalpha():
                y = AlphabetMap[char]
                a_inv = pow(self.a, -1, 26)
                x = (a_inv * (y - self.b)) % 26
                plaintext += ReverseAlphabetMap[x]
            else:
                plaintext += char
        return plaintext
    
    
    