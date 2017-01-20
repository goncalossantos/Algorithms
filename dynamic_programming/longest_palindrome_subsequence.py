def lps(sequence: str) -> str:
    """ Longest Palindrome Subsequence

    :param sequence: input string
    :return: Returns the reconstructed palindrome
    """

    l_sequence = list(sequence)
    l = len(l_sequence)
    # Structure to hold the dynamic programming tabulated results
    # It is bigger than what is needed, it is N^2 but we only need space for all the pair of indexes combinations in
    # the sequence
    dp = [[(0, [], (None, None)) for _ in l_sequence] for _ in l_sequence]
    i = 0
    while i < l:
        # i is the difference between index one and 2
        for j in range(0, l - i):
            # j is index one, k is index two
            k = j + i
            if l_sequence[k] == l_sequence[j]:
                # if the letters are the same, either...
                if (k - j) > 1:
                    # the letters are separated by more than one letter, wich means 2 + the lps between them
                    dp[j][k] = (2 + dp[j + 1][k - 1][0], [l_sequence[j], l_sequence[k]], (j + 1, k - 1))
                elif k == j:
                    # the indexes are the same, which means the lps is one (either one of them)
                    dp[j][k] = (1, [l_sequence[j]], (None, None))
                else:
                    # the letters are right next to each other, which means the lps is 2 (both of them)
                    dp[j][k] = (2, [l_sequence[j], l_sequence[k]], (None, None))
            else:
                # The letters don't match, so the lps is either contained in the left part (j to k-1) or in the
                # right part (j+1 to k)
                if dp[j][k - 1][0] >= dp[j + 1][k][0]:
                    dp[j][k] = (dp[j][k - 1][0], [""], (j, k - 1))
                else:
                    dp[j][k] = max(dp[j][k - 1], dp[j + 1][k], key=lambda x: x[0])
        i += 1

    return reconstruct(dp)


def reconstruct(dp):
    """ Reconstructs the lps by a kind of "parent" method

    :param dp:
    :return:
    """
    next_char = max(max(row, key=lambda x: x[0]) for row in dp)
    left = []
    right = []
    while next_char:
        chars = next_char[1]
        if len(chars) == 2:
            left.append(chars[0])
            right.append(chars[1])
        elif len(chars) == 1:
            left.append(chars[0])
        new_x, new_y = next_char[2]
        if new_x and new_y:
            next_char = dp[new_x][new_y]
        else:
            next_char = None
    return "".join(left + list(reversed(right)))
