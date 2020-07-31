def bubble_sort(unsorted_array):
    for i in range(len(unsorted_array)-1, 0, -1):
        for j in range(i):
            if unsorted_array[j] > unsorted_array[j+1]:
                unsorted_array[j], unsorted_array[j + 1] = unsorted_array[j + 1], unsorted_array[j]
    print(unsorted_array)


bubble_sort([2, 4, 1, 5, 7, 8, 1, 7])

