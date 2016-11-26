
"""
@param a: The first integer
@param b: The second integer
@return:  The sum of a and b
Complexity: O(log(b)) or O(n_bits_b)
"""
def aplusb(a, b):

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

def test_aplusb():

    assert aplusb(4,3) == 7
    assert aplusb(0,3) == 3
    assert aplusb(-4,3) == -1
