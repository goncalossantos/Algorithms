class EditDistance(object):
    """ Main interface to solving the Edit Distance problem

    """

    @classmethod
    def recursive(cls, x: str, y: str) -> int:
        """ Naive recursive solution for edit distance

        :param x: string 1
        :param y: string 2
        :return: returns the minimum number of edits required to make x == y
        """

        if not x and not y:
            return 0
        elif not x or not y:
            return max(len(x), len(y))

        if x[-1] == y[-1]:
            result = EditDistance.recursive(x[:-1], y[:-1])
        else:
            result = min(
                EditDistance.recursive(x[:-1], y[:-1]),  # Replace
                EditDistance.recursive(x[:-1], y),  # Insert/Remove
                EditDistance.recursive(x, y[:-1]),  # Insert/Remove
            ) + 1
        return result

    @classmethod
    def tabulation(cls, x: str, y: str) -> int:
        """ Dynamic programming solution for edit distance

        the complexity of this method is O(mn), with m beign the length of x and n the length of y.

        :param x: string 1
        :param y: string 2
        :return: returns the minimum number of edits required to make x == y

        """
        # TODO find a way to return all the edits required

        rows = len(x)  # type:int
        cols = len(y)  # type:int
        tabulated_results = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(rows + 1):
            for j in range(cols + 1):
                if i == 0:
                    tabulated_results[i][j] = j
                if j == 0:
                    tabulated_results[i][j] = j
                if x[i - 1] == y[j - 1]:
                    tabulated_results[i][j] = tabulated_results[i - 1][j - 1]
                else:
                    tabulated_results[i][j] = min(
                        tabulated_results[i - 1][j - 1],
                        tabulated_results[i - 1][j],
                        tabulated_results[i][j - 1],
                    ) + 1
        return tabulated_results[rows][cols]
