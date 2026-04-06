class playfair:
    def __init__(self, key : str):
        self.key = key
    def generate_key_matrix(self):
        key_matrix = []
        for char in self.key.upper():
            if char.isalpha() and char not in key_matrix:
                key_matrix.append(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in key_matrix:
                key_matrix.append(char)
        return [key_matrix[i:i+5] for i in range(0, 25, 5)]
    def encrypt(self, plaintext):
        matrix = self.generate_key_matrix()
        ciphertext = ""
        plaintext = plaintext.replace(" ", "").upper()
        i = 0
        while i < len(plaintext):
            char1 = plaintext[i].upper()
            i += 1
            if(i < len(plaintext) and plaintext[i].upper() != char1):
                char2 = plaintext[i].upper()
                i += 1
            else:
                char2 = 'X'
                
            print(f"Encrypting pair: {char1} {char2}")
            for row in matrix:
                if char1 in row:
                    row1, col1 = matrix.index(row), row.index(char1)
                if char2 in row:
                    row2, col2 = matrix.index(row), row.index(char2)
            if row1 == row2:
                ciphertext += matrix[row1][(col1 + 1) % 5] # i put %5 to wrap around the matrix
                ciphertext += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += matrix[(row1 + 1) % 5][col1]
                ciphertext += matrix[(row2 + 1) % 5][col2]
            else:
                ciphertext += matrix[row1][col2]
                ciphertext += matrix[row2][col1]
        return ciphertext
    def decrypt(self, ciphertext):
        matrix = self.generate_key_matrix()
        plaintext = ""
        ciphertext = ciphertext.replace(" ", "").upper()
        i = 0
        while i < len(ciphertext):
            char1 = ciphertext[i].upper()
            i += 1
            char2 = ciphertext[i].upper()
            i += 1
            print(f"Decrypting pair: {char1} {char2}")
            for row in matrix:
                if char1 in row:
                    row1, col1 = matrix.index(row), row.index(char1)
                if char2 in row:
                    row2, col2 = matrix.index(row), row.index(char2)
            if row1 == row2:
                plaintext += matrix[row1][(col1 -1) % 5]
                plaintext += matrix[row2][(col2 -1) % 5]
            elif col1 == col2:
                plaintext += matrix[(row1 - 1) % 5][col1]
                plaintext += matrix[(row2 - 1) % 5][col2]
            else:
                plaintext += matrix[row1][col2]
                plaintext += matrix[row2][col1]
        return plaintext

