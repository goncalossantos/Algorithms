class Rotation():

    def rotate(self, i, j):
        return (j, self.N - i -1)

    def __init__(self, i, j, N):
        self.N = N
        self.get_coordinates_to_rotate(i, j)

    def get_coordinates_to_rotate(self, i, j):

        self.top = (i,j)
        self.right = self.rotate(i,j)
        self.bottom = self.rotate(*self.right)
        self.left = self.rotate(*self.bottom)


def apply_rotation(matrix, rotation):

    tmp = matrix[rotation.top[0]][rotation.top[1]]

    matrix[rotation.top[0]][rotation.top[1]] = matrix[rotation.left[0]][rotation.left[1]]
    matrix[rotation.left[0]][rotation.left[1]] = matrix[rotation.bottom[0]][rotation.bottom[1]]
    matrix[rotation.bottom[0]][rotation.bottom[1]] = matrix[rotation.right[0]][rotation.right[1]]
    matrix[rotation.right[0]][rotation.right[1]] = tmp

    return matrix

def rotate_matrix(matrix):
    """Rotates a matrix 90 degrees
    
    Iterates through a matrix to rotate it in place.
    
    Arguments:
        matrix {list of lists} -- contains the matrix of ints
    
    Returns:
        [list of lists] -- rotated matrix
    """

    N = len(matrix)
    # We only need to go to the middle row
    for i in range(N/2):
        # We only need to to the inside columns
        for j in range(i,N-i-1):
            rotation = Rotation(i, j, N)
            matrix = apply_rotation(matrix, rotation)

    return matrix


def print_matrix(matrix):

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))

def test_matrix():

    test_2 = ([[1, 2], [3, 4]] , [[3, 1], [4, 2]])
    test_3 = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    test_4 = (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]],
    )


    for test in [test_2, test_3, test_4]:
        result = rotate_matrix(test[0])
        assert result == test[1]


test_matrix()