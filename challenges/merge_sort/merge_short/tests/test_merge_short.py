from merge_short.merge_sort import merge_sort

def test_simple_arr():
    arr = [8,4,23,42,16,15]
    merge_sort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]


