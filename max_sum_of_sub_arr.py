def max_sum2(arr):
    sums = []
    for i in range(len(arr)):
        for j in range(len(arr)):

            if sum(arr[j:i + 1]) != 0:
                sums.append(sum(arr[j:i + 1]))

    return max(sums)


def max_sum(arr):
    return max(
        [sum(arr[j:i + 1]) if sum(arr[j:i + 1]) != 0 else -1000 for j in range(len(arr)) for i in range(len(arr))])


print(max_sum([-2, -1]))
