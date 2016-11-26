
def check_for_replace(s1, s2):

    # Just to make sure
    assert len(s1) == len(s2)

    lenght = len(s1)
    differences = 0

    for i in range(lenght):
        if s1[i] != s2[i]:
            differences += 1
        if differences > 1:
            return False

    return True


def check_insert_or_replace(s1, s2):

    # Just to make sure
    assert len(s1) == (len(s2) + 1) or (len(s1) + 1) == (len(s2))

    smaller, bigger = (s1, s2) if s1 < s2 else (s2, s1)

    j = 0
    for i in range(len(smaller)):
        if smaller[i] != bigger[j]:
            if j != i:
                return False
            j += 1
        j += 1

    return True


def one_edit_away(s1, s2):

    if len(s1) == len(s2):
        return check_for_replace(s1, s2)
    if len(s1) == (len(s2) + 1) or (len(s1) + 1) == (len(s2)):
        return check_insert_or_replace(s1, s2)
    return False


def test_one_edit_away():
    assert one_edit_away("aaaa", "aaab")
    assert one_edit_away("aaaa", "aaa")
    assert one_edit_away("aaaa", "aaaaa")
    assert one_edit_away("aaaa", "aaaa")

    assert not one_edit_away("aaaa", "bbbb")
    assert not one_edit_away("aaaa", "aabb")
    assert not one_edit_away("aaaa", "aaaaaa")
    assert not one_edit_away("aaaaaa", "aaaa")

    assert one_edit_away("aaaa", "aaaab")
    assert one_edit_away("aaaab", "aaaa")

    assert not one_edit_away("aaaa", "")
    assert not one_edit_away("", "aaaa")
