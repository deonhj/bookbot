from stats import get_num_words, get_num_chars, get_count_per_char

def main():
    file_content = get_book_text('books/frankenstein.txt')
    print(f"{get_num_words(file_content)} words found in the document.")
    print(f"{get_num_chars(file_content)} characters found in the document.")
    print(get_count_per_char(file_content.lower()))


def get_book_text(file_path):
    """
    Reads the contents of a text file, and returns the text.
    """

    with open(file_path) as file:
        return file.read()


if __name__ == "__main__":
    main()




