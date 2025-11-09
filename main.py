from sys import argv
from stats import get_num_chars, get_num_words

def output_results(num_words: int, char_counter: dict):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in sorted(char_counter.items(), key=lambda t: -t[1]):
        print(f"{k}: {v}")
    print("============= END ===============")

def get_file_name():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    return argv[1]

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    book_file_name = get_file_name()
    book_text = get_book_text(book_file_name)
    words_count = get_num_words(book_text)
    chars_count = get_num_chars(book_text)
    output_results(words_count, chars_count)

if __name__ == "__main__":
    main()
