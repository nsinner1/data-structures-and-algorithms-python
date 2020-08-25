## Merge Sort
Merge sort breaks a list up into the smaller lists than merges the lists back together in order.

## Pseudocode

```
 ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

## Trace
#### Sample array: [8,4,23,42,16,15]

### Pass 1-6 Visual 
! [Drawing of each pass](assets/merge_sort.jpeg)

### Pass 1:

Merge sort divides our list by half, than its left and right part on half and so on at the same time inside each merge_sort() function call we are calling merge() function and passing to it the current left, right, and part of the list. The merge() function should merge in proper order all elements from left and right.

### Pass 2:

Merge(left, right, arr) function will start form the bottom of our "tree". [4] will be left list, [23] right list, [4, 23] the arr. After merging 4 and 23, arr stays [4, 23]. 

### Pass 3:

Merge() will be called with ([8], [4, 23], [8, 4, 23]) as parameters. After merging arr became [4, 8, 23]

### Pass 4: 

Merge() finished with the left part of our "tree" and goes to the right branches. Merge will be called with ([16], [15], [16, 15]) as parameters. After merging arr became [15, 16]

### Pass 5:

Merge() will be called with ([42], [15, 16], [42, 16, 15]) as parameters. After merging and proper ordering arr became [15, 16, 42]

### Pass 6:

Now the "tree" has two ordered sublists. Call merge last tme with this sublists and our list as parameters. Our lists merged and all elements are ordered.


#### Sorted array: [4, 8, 15, 16, 23, 42]

## Efficiency
* Space complexity Big O(n)
* Time complexity Big O(nLogn)