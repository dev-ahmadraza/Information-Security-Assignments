def caesar_encrypt(text, shift):
    result = ""  # This will store the final encrypted text

    for char in text:  # Loop through each character in the input text
        
        if char.isalpha():  # Check if character is a letter
            
            if char.isupper():  # If the letter is uppercase (A-Z)
                # Convert letter to number, shift it, wrap using %26, convert back
                new_char = chr((ord(char) + shift - 65) % 26 + 65)
            
            else:  # If the letter is lowercase (a-z)
                new_char = chr((ord(char) + shift - 97) % 26 + 97)
            
            result += new_char  # Add shifted letter to result
        
        else:
            result += char  # Keep spaces and symbols unchanged

    return result  # Return encrypted text

def caesar_decrypt(text, shift):
    result = ""  # This will store the decrypted text

    for char in text:  # Loop through each character
        
        if char.isalpha():  # Check if it is a letter
            
            if char.isupper():  # For uppercase letters
                new_char = chr((ord(char) - shift - 65) % 26 + 65)
            
            else:  # For lowercase letters
                new_char = chr((ord(char) - shift - 97) % 26 + 97)
            
            result += new_char  # Add original letter
        
        else:
            result += char  # Keep spaces/symbols same

    return result  # Return decrypted text

# Take input from user
text = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encrypt the message
encrypted = caesar_encrypt(text, shift)
print("Encrypted:", encrypted)

# Decrypt the message
decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:", decrypted)