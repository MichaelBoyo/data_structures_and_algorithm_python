def find_sum(arr, k):
    tmp = []
    for i in range(len(arr)):
        if len(arr[:k]) < k:
            return max(tmp)
        tmp.append(sum(arr[:k]))
        arr.pop(0)

    return max(tmp)


def find_sum2(arr, k):
    val = 0
    for i in arr:
        if len(arr[:k]) < k:
            return val
        if sum(arr[:k]) > val:
            val = sum(arr[:k])
        arr.pop(0)

    return val


print(find_sum2([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
