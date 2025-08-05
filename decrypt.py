def caesar_decrypt(text, shift):
    """Decrypt text using Caesar cipher with the given shift."""
    decrypted = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted


def brute_force_decrypt(text):
    """
    Try all 26 Caesar shifts and return the correct decryption
    based on detection of common English words.
    """
    common_words = ["the", "and", "is", "message", "secret"]

    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        found = sum(word in decrypted for word in common_words)
        if found >= 2:  # נניח ש-2 מילים מספיקות לזיהוי
            return shift, decrypted

    return None, "No valid decryption found."
