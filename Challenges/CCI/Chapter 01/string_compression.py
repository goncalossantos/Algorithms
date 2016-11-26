
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
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)


def test_string_compression():

    assert string_compression("aaaaaa") == "a6"
    assert string_compression("aaabbb") == "a3b3"
    assert string_compression("aaabbbcdd") == "a3b3c1d2"
    assert string_compression("aabbbcdd") == "aabbbcdd"
    assert string_compression("abcd") == "abcd"
