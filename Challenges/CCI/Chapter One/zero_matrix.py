def set_array_for_zeroing(matrix, i, j, r, c):

    for ii in range(0,r):
        matrix[ii][j] = (matrix[ii][j][0], 0)
    for jj in range(0,c):
        matrix[i][jj] = (matrix[i][jj][0], 0)
    return matrix



def zero_matrix(matrix):

    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = (matrix[i][j], 1)


    for i in range(rows):
        for j in range(columns):
            if matrix[i][j][0] == 0:
                matrix = set_array_for_zeroing(matrix, i, j, rows, columns)


    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j][1] == 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i][j][0]

    return matrix


def test_zero_matrix():
    
    test_1 = ([[1, 2, 3], [4, 0, 6], [7, 8, 9]], [[1, 0, 3], [0, 0, 0], [7, 0, 9]])
    test_2 = ([[1, 0, 3], [4, 5, 6], [7, 0, 9]], [[0, 0, 0], [4, 0, 6], [0, 0, 0]])
    test_3 = ([[0, 2, 3], [4, 5, 6], [7, 8, 0]], [[0, 0, 0], [0, 5, 0], [0, 0, 0]])

    for test in [test_1, test_2, test_3]:

        result = zero_matrix(test[0])
        assert result == test[1]

test_zero_matrix()