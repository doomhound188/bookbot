from stats import get_num_words
from stats import get_num_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_content)
    char_count = get_num_characters(book_content)
    print(f"{num_words} words found in the document")
    print(f"{char_count}")

if __name__ == "__main__":
    main()