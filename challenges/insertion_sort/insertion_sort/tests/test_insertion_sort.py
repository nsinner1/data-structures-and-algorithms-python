from insertion_sort.insertion_sort import insertion_sort

def test_simple_lst():
    lst = [8,4,23,42,16,15]
    insertion_sort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]
