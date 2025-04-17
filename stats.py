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
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


def report(chars):

    char_dict = get_count_per_char(chars)
    report_list = []
    for char in char_dict:
        report_list.append({"char":char, "occurences":char_dict[char]})

    def sort_on(dict):
        return dict["occurences"]

    report_list.sort(reverse=True, key=sort_on)

    for char in report_list:
        print(f"{char["char"]}: {char["occurences"]}")



    
