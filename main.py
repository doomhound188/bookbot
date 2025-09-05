import sys
from stats import get_num_words, get_num_characters, sort_chars

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # Validate CLI usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Take book path from CLI argument
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    # Word count
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    char_count = get_num_characters(text)
    sorted_chars = sort_chars(char_count)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()