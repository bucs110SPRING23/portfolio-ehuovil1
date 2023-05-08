import random

# Define the original and substitution alphabets
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
substitution = "XPMKJCFRSTOYBLHUVNWGADQZEI"

# Generate a random permutation of the substitution alphabet
substitution_permuted = ''.join(random.sample(substitution, len(substitution)))

def encrypt(plaintext):
    """
    Encrypts the plaintext using the substitution cipher.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Only alter alphabetical characters
            if char.islower():  # Preserve the case of the character
                ciphertext += substitution_permuted[alphabet.index(char.upper())].lower()
            else:
                ciphertext += substitution_permuted[alphabet.index(char)]
        else:
            ciphertext += char  # Leave non-alphabetical characters unchanged
    return ciphertext

# Input plaintext
plaintext = "The quick brown fox jumps over the lazy dog"

# Encrypt plaintext
ciphertext = encrypt(plaintext)

# Write encrypted text to file
with open("encrypted.txt", "w") as file:
    file.write(ciphertext)
