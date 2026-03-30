class testing:
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

def main() :
    print("This is a test file for the alphabet mapping")

    testing1 = testing(3)
    plaintext = "HELLO WORLD vwxyz white"
    print ("Plaintext: ", plaintext.upper())
    ciphertext = testing1.encrypt(plaintext)
    print ("Ciphertext: ", ciphertext)
    decryptedtext = testing1.decrypt(ciphertext)
    print ("Decryptedtext: ", decryptedtext)

main()
