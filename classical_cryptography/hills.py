from alphabet.alphabet import AlphabetMap, ReverseAlphabetMap

class hills:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate_first_letter(self, char1: str, char2: str) -> int:
        x1 = AlphabetMap[char1]
        x2 = AlphabetMap[char2]
        return (self.a * x1 + self.b * x2) % 26
    
    def calculate_second_letter(self, char1: str, char2: str) -> int:
        x1 = AlphabetMap[char1]
        x2 = AlphabetMap[char2]
        return (self.c * x1 + self.d * x2) % 26
    
    def encrypt(self, plaintext):
        ciphertext = ""
        plaintext = plaintext.replace(" ", "").upper()
        for i in range(0, len(plaintext), 2):
            char1 = plaintext[i].upper()
            char2 = plaintext[i+1].upper() if i+1 < len(plaintext) else 'X'
            ciphertext += ReverseAlphabetMap[self.calculate_first_letter(char1, char2)]
            ciphertext += ReverseAlphabetMap[self.calculate_second_letter(char1, char2)]
        return ciphertext
    
    def matrice_inverse(self):
        determinant = (self.a * self.d - self.b * self.c) % 26
        determinant_inv = pow(determinant, -1, 26)
        a_inv = (self.d * determinant_inv) % 26
        b_inv = (-self.b * determinant_inv) % 26
        c_inv = (-self.c * determinant_inv) % 26
        d_inv = (self.a * determinant_inv) % 26
        return a_inv, b_inv, c_inv, d_inv
    
    def decrypt(self, ciphertext):
        plaintext = ""
        ciphertext = ciphertext.replace(" ", "").upper()
        for i in range(0, len(ciphertext), 2):
            char1 = ciphertext[i].upper()
            char2 = ciphertext[i+1].upper() if i+1 < len(ciphertext) else 'X'
            x1 = AlphabetMap[char1]
            x2 = AlphabetMap[char2]
            a_inv, b_inv, c_inv, d_inv = self.matrice_inverse()
            plaintext += ReverseAlphabetMap[(a_inv * x1 + b_inv * x2) % 26]
            plaintext += ReverseAlphabetMap[(c_inv * x1 + d_inv * x2) % 26]
        return plaintext
        
        