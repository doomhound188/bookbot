def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

def get_num_characters(book_text):
    chars = {}
    text = book_text.lower()
    for char in text:
        chars[char] = chars.get(char, 0) + 1
    return chars