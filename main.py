from stats import get_num_words, get_num_characters, sort_chars

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


    char_count = get_num_characters(text)
    sorted_chars = sort_chars(char_count)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()