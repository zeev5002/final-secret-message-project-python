def analyze_text(text):
    """Analyze the decrypted text using built-in functions."""
    words = text.split()
    vowels = 'aeiou'

    word_count = len(words)
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    unique_chars = len(set(text.replace(" ", "")))

    total_letters = sum(1 for c in text if c.isalpha())
    vowel_count = sum(1 for c in text if c.lower() in vowels)
    vowel_percentage = round((vowel_count / total_letters) * 100, 2) if total_letters > 0 else 0

    sorted_by_length = sorted(words, key=len)
    all_lowercase = all(word.islower() for word in words)
    any_long_word = any(len(word) > 7 for word in words)

    indexed_words = list(enumerate(words))
    word_length_pairs = list(zip(words, map(len, words)))

    return {
        "word_count": word_count,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "unique_chars": unique_chars,
        "vowel_percentage": vowel_percentage,
        "sorted_by_length": sorted_by_length,
        "all_lowercase": all_lowercase,
        "any_long_word": any_long_word,
        "indexed_words": indexed_words,
        "word_length_pairs": word_length_pairs
    }
