from decrypt import brute_force_decrypt
from analysis import analyze_text


def read_encrypted_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def main():
    encrypted_text = read_encrypted_file('encrypted.txt')
    shift, decrypted = brute_force_decrypt(encrypted_text)

    print("Detected shift:", shift)
    print("Decrypted text:\n", decrypted)

    print("\n--- Text Analysis ---")
    analysis = analyze_text(decrypted)
    print("Word count:", analysis["word_count"])
    print("Longest word:", analysis["longest_word"])
    print("Shortest word:", analysis["shortest_word"])
    print("Unique characters:", analysis["unique_chars"])
    print("Vowel percentage:", analysis["vowel_percentage"], "%")
    print("Sorted by length:", analysis["sorted_by_length"])
    print("All words lowercase:", analysis["all_lowercase"])
    print("Any word longer than 7 letters:", analysis["any_long_word"])
    print("Indexed words:", analysis["indexed_words"])
    print("Word-length pairs:", analysis["word_length_pairs"])


if __name__ == "__main__":
    main()
