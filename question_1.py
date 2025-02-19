import string

def shift_forward(char, shift, base):
    """ Shifts character forward. """
    return chr(((ord(char) - base + shift) % 26) + base)

def shift_backward(char, shift, base):
    """ Shifts character backward. """
    return chr(((ord(char) - base - shift) % 26) + base)

def encrypt(text, n, m):
    """
    Encrypts the text following the given instructions.
    """
    encrypted_text = ""

    for char in text:
        if 'a' <= char <= 'm':  # First half of lowercase
            encrypted_text += shift_forward(char, n * m, ord('a'))
        elif 'n' <= char <= 'z':  # Second half of lowercase
            encrypted_text += shift_backward(char, n + m, ord('a'))
        elif 'A' <= char <= 'M':  # First half of uppercase
            encrypted_text += shift_backward(char, n, ord('A'))
        elif 'N' <= char <= 'Z':  # Second half of uppercase
            encrypted_text += shift_forward(char, m ** 2, ord('A'))
        else:  # Non-alphabetic characters unchanged
            encrypted_text += char  

    return encrypted_text

def decrypt(encrypted_text, n, m):
    """
    Decrypts the text via reverseing instructions:
    """
    decrypted_text = ""

    for char in encrypted_text:
        if 'a' <= char <= 'm':  # First half of lowercase
            decrypted_text += shift_backward(char, n * m, ord('a'))
        elif 'n' <= char <= 'z':  # Second half of lowercase
            decrypted_text += shift_forward(char, n + m, ord('a'))
        elif 'A' <= char <= 'M':  # First half of uppercase
            decrypted_text += shift_forward(char, n, ord('A'))
        elif 'N' <= char <= 'Z':  # Second half of uppercase
            decrypted_text += shift_backward(char, m ** 2, ord('A'))  # Potential error*
        else:  # Non-alphabetic characters unchanged
            decrypted_text += char  

    return decrypted_text

def verify(original_text, decrypted_text):
    """ Checks if decrypted text matches original. """
    return original_text.strip() == decrypted_text.strip()

def main():
    """
    Handles:
    - Input
    - Reading & writing
    - Encryption & decryption
    - Verification
    """
    # Obtain values to shift text
    n = int(input("Enter a value for n: "))  
    m = int(input("Enter a value for m: "))  

    # Read original text
    with open("raw_text.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()

    # Encrypt
    encrypted_text = encrypt(raw_text, n, m)

    # Write encrypted text
    with open("encrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    # Decrypt
    decrypted_text = decrypt(encrypted_text, n, m)

    # Write decrypted text
    with open("decrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(decrypted_text)

    # Debugging
    print("\n=== DEBUGGING ===")
    print("Original:", repr(raw_text))
    print("\nEncrypted:", repr(encrypted_text))
    print("\nDecrypted:", repr(decrypted_text))

    # Check if correct
    if verify(raw_text, decrypted_text):
        print("The decryption is a success. The text matches the raw text.")
    else:
        print("Th decryption has failed! The text does not match.")

# Main function runs
if __name__ == "__main__":
    main()

