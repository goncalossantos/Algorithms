from typing import List


def lcs(x: str, y: str) -> int:
    """ Computes the longest common subsequence between two strings

    This function uses dynamic programming in the form of tabulation.
    The most import thing is that, given a string X with length M and a string Y with length N,
    the following is known about the LCS:
        LCS(X[:M],Y[:N) = (LCS(X[:M-1], Y[:N-1]) + 1) if X[M]=Y[N] else max(LCS(X[:M], Y[:N-1]), LCS(X[:M-1], Y[:N]))

    Therefore, this problem could easily be solved recursively, but recursion is very inefficient because it
    recalculates a lot of the results. This problem has optimal substructure and overlapping sub-problems, so it
    can be solved using dynamic programming.

    The tabulation approach below calculates all the LCS results only once in a bottom up approach,
    stores them in a matrix and re-uses them.

    :param x: first string
    :param y: second string
    :return: Returns the length of the longest common subsequence
    """

    # Null case
    if not x or not y:
        return 0

    # initialize matrix for tabulated results. This matrix has an auxiliary first column and row for the -1 indexes
    rows = len(x)  # type:int
    cols = len(y)  # type:int
    lcs_matrix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]  # type:List[List[int]]

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if x[r - 1] == y[c - 1]:
                lcs_matrix[r][c] = (lcs_matrix[r - 1][c - 1] + 1)
            else:
                lcs_matrix[r][c] = max(lcs_matrix[r - 1][c], lcs_matrix[r][c - 1])
    return lcs_matrix[rows][cols]
