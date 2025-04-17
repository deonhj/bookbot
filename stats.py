def get_num_words(file_content):
    """
    Counts the number of words in the given text.
    """

    words = file_content.split()
    return len(words)

def get_num_chars(file_content):
    """
    Counts the number of characters in the given text.
    """

    return len(file_content)


def get_count_per_char(file_content):
    """
    Counts the number of occurrences of each character in the given text.
    """

    count = {}
    for char in file_content.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


