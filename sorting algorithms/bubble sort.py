def bubble_sort(unsorted_array):
    pass_cnt = 0
    for i in range(len(unsorted_array)-1, 0, -1):
        check = 0
        for j in range(i):
            if unsorted_array[j] > unsorted_array[j+1]:
                unsorted_array[j], unsorted_array[j + 1] = unsorted_array[j + 1], unsorted_array[j]
                check += 1
        if check == 0:
                break
        pass_cnt += 1
    print(f"It took {pass_cnt} passes to sort the array")
    print(unsorted_array)


bubble_sort([2, 4, 1, 5, 7, 8, 1, 7])

