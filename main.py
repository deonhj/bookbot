def main():
    file_content = get_book_text('books/frankenstein.txt')
    print(f"{get_word_count(file_content)} words found in the document.")


def get_book_text(file_path):
    """
    Reads the contents of a text file, and returns the text.
    """

    with open(file_path) as file:
        return file.read()


if __name__ == "__main__":
    main()




