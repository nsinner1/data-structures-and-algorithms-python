from quick_sort.quick_sort import quick_sort


def test_simple_arr():
    lst = [8,4,23,42,16,15]
    quick_sort(lst, 0, 5)
    assert lst == [4, 8, 15, 16, 23, 42]
