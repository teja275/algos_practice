def insertion_sort(unsorted_array):
    sorted_array = []
    for key in unsorted_array:
        if (len(sorted_array) == 0) or (key <= sorted_array[0]):
            sorted_array.insert(0, key)
        elif key >= sorted_array[-1]:
            sorted_array.append(key)
        else:
            for j in range(len(sorted_array)):
                find = 0
                if (key >= sorted_array[j]) and (key <= sorted_array[j+1]):
                    sorted_array.insert(j+1, key)
                    find += 1
                if find > 0:
                    break
    print(sorted_array)


# insertion_sort([2, 4, 1])
insertion_sort([2, 4, 1, 5, 7, 8, 1, 7])


