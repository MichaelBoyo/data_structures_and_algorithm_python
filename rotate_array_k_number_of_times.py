def rotate_array_k_number_of_times(arr, k):
    for i in range(k + 1):
        a = arr.pop(0)
        arr.append(a)
    return arr


print(rotate_array_k_number_of_times([1, 2, 3, 4, 5, 6, 7], 3))
