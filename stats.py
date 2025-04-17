def get_word_count(file_content):
    """
    Counts the number of words in the given text.
    """

    words = file_content.split()
    return len(words)