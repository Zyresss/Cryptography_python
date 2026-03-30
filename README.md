# Cryptography_python
some cryptography methods

## Classic Ciphers 

1. Caesar Cipher :
    - shift each character by a fixed number of positions in the alphabet.
    * caesar_encrypt(text_to_encrypt, shift)
    * caesar_decrypt(text_to_decrypt, shift)

2. Affine Cipher :
    - uses E(x) = (ax + b) mod m .
    * affine_encrypt(text_to_encrypt, a, b)
    * affine_decrypt(text_to_decrypt, a, b)

3. Vigenere Cipher :
    - uses repeating key word.
    * vigenere_encrypt(text_to_encrypt, key)
    * vigenere_decrypt(text_to_decrypt, key)

4. Playfair Cipher :
    - encrypts pair of letters using a 5x5 grid of letters.
    * playfair_encrypt(text_to_encrypt, key)
    * playfair_decrypt(text_to_decrypt, key)

5. Hill Cipher :
    - algebra-based cipher method encrypts group of letters using matrix multiplication.
    * hill_encrypt(text_to_encrypt, key_matrix)
    * hill_decrypt(text_to_decrypt, key_matrix)

## Symmetric Ciphers

1. RC4 :
    - encrypts data byte by byte by generating keystream combined with plaintext using XOR operation.
    * rc4_encrypt(text_to_encrypt, key)
    * rc4_decrypt(text_to_decrypt, key)

2. AES (Advanced Encryption Standard) :
    - 
    * aes_encrypt(text_to_encrypt, key)
    * aes_decrypt(text_to_decrypt, key)

3. DES (Data Encryption Standard) :
    - 
    * des_encrypt(text_to_encrypt, key)
    * des_decrypt(text_to_decrypt, key)

## Asymmetric Ciphers

1. RSA (Rivest-Shamir-Adleman) :
    - 
    * rsa_encrypt(m, e, n)
    * rsa_decrypt(c, d, n)

