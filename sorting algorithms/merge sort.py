def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array)//2

        left_array = unsorted_array[:mid]
        right_array = unsorted_array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        len_left = len(left_array)
        len_right = len(right_array)
        i = 0
        j = 0
        k = 0
        while (i < len_left) & (j < len_right):
            if left_array[i] <= right_array[j]:
                unsorted_array[k] = left_array[i]
                i += 1
            else:
                unsorted_array[k] = right_array[j]
                j += 1
            k += 1
        while i < len_left:
            unsorted_array[k] = left_array[i]
            i += 1
            k += 1
        while j < len_right:
            unsorted_array[k] = right_array[j]
            j += 1
            k += 1


my_list = [2, 4, 1, 5, 7, 8, 1, 7]
print(f"Unsorted list is {my_list}")
merge_sort(my_list)
print(f"Sorted list is {my_list}")
