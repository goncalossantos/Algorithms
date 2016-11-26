
def is_substring(x,y):
    return x in y


def is_rotation(x,y):

    extended_y = y + y
    return x in extended_y


def test_is_rotation():

    assert is_rotation("water","aterw")
    assert is_rotation("wat er","at erw")
    assert is_rotation("waterbottle","erbottlewat")