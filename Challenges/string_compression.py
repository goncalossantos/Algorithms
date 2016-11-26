
def get_compressed(char, count):
    """ Compress a substring ""

    Given a character and a a count, return "char"+str(count)
    Example: get_compressed("a",5) = "a5"
    """
    compressed = ''
    if char:
        compressed = char + str(count)
    return compressed


def string_compression(string):

    output_string = ''

    current_count = 0
    current_char = ''

    for char in string:
        if current_char != char:
            # Get the compressed part if count is bigger than one
            output_string += get_compressed(current_char, current_count)
            if len(output_string) >= len(string):
                return string
            # Update the char and the count
            current_char = char
            current_count = 1
        else:
            current_count += 1
    output_string += get_compressed(current_char, current_count)
    return output_string if len(output_string) < len(string) else string


def test_string_compression():

    assert string_compression("aaaaaa") == "a6"
    assert string_compression("aaabbb") == "a3b3"
    assert string_compression("aaabbbcdd") == "a3b3c1d2"
    assert string_compression("aabbbcdd") == "aabbbcdd"
    assert string_compression("abcd") == "abcd"
