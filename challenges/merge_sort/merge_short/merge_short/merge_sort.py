def merge_sort(arr):

    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[: mid]
        right = arr[mid:]

        # sort the left side
        merge_sort(left)

        # sort the right side
        merge_sort(right)


        # merge the sorted left and right sides together
        merge(left, right, arr)

def merge(left, right, arr):

    i = 0
    j = 0
    k = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        for entries in right[j:]:
            arr[k] = entries
            k += 1

    else:
        for entries in left[i:]:
            arr[k] = entries
            k +=1