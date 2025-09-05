def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

def get_num_characters(book_text):
    chars = {}
    text = book_text.lower()
    for char in text:
        chars[char] = chars.get(char, 0) + 1
    return chars

def sort_chars(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    char_list.sort(key=sort_on, reverse=True)
    return char_list