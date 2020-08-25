## Insertion Sort
Insertion sort is a type of sorting algorithm that traverses an array multiple times as it builds out the results.

## Pseudocode

```
InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
```

## Trace
#### Sample array: [8,4,23,42,16,15]

### Pass 1-6 Visual 
! [Drawing of each pass](assets/insertion_sort.jpeg)

### Pass 1:

We start with the first element in the array (8). Then we consider the next element in the array(4). 4 is smaller than 8, so we swap them.

### Pass 2:

We consider the second element (8) in the array. 8 is the next smallest number so we left it in the same place.

### Pass 3:

We consider the third element (23) in the array. It is bigger than 16 and 15 but smaller then 42.  Since 15 is the next smallest number in the array, 23 and 15 swap. 

### Pass 4: 

We consider the forth element (42) in the array. 16 is the smallest number so 42 and 16 swap. 

### Pass 5:

We consider the fifth element (42) in the array. 16 is the smallest number so 42 and 23 swap. 

### Pass 6:

We consider the sixth element (42) in the array, it will swap with itself as it is comparing to itself as there are no more element left in the array. 

#### Sorted array: [4, 8, 15, 16, 23, 42]
## Efficiency
* Space complexity Big O(1)
* Time complexity Big O(n^2)
