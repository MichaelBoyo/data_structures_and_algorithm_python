def sum_sub_array_min(arr):
    subs = []
    k = 1
    while k <= len(arr):
        for i in range(len(arr)):
            a = arr[i:k]
            if a:
                subs.append(max(a))
        k += 1

    return sum(subs)


print(sum_sub_array_min([4,1,2,3,4]))
