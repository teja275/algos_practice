def selection_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        for j in range(i, len(unsorted_array)):
            if unsorted_array[j] < unsorted_array[i]:
                unsorted_array[i], unsorted_array[j] = unsorted_array[j], unsorted_array[i]
    print(unsorted_array)


selection_sort([2, 4, 1, 5, 7, 8, 1, 7])
