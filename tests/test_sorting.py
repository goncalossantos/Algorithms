import pytest
from ..Sorting.sorting import insertion_sort


@pytest.fixture(
    params=[
        ([1, 3, 2, 10, 4, 2], [1, 2, 2, 3, 4, 10]),
        ([1, -3, -2, 10, 4, 2, -15, 0], [-15, -3, -2, 0, 1, 2, 4, 10]),
    ]
)
def sort_test_input(request):
    return request.param


def test_insertion_sort(sort_test_input):

    input = sort_test_input[0]
    sorted = sort_test_input[1]
    assert insertion_sort(input) == sorted
