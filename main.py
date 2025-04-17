from stats import get_num_words, get_num_chars, get_count_per_char, report
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    
    file_content = get_book_text(sys.argv[1])
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(file_content)} total words")
    print("--------- Character Count -------")
    report(file_content)
    print("============= END ===============")

def get_book_text(file_path):
    """
    Reads the contents of a text file, and returns the text.
    """

    with open(file_path) as file:
        return file.read()


if __name__ == "__main__":
    main()




