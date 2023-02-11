def permutation(n: int, m: int, k) -> bool:
    if n == 0:
        return False
    if n % 2 == 1:
        return True
    return permutation(n - m, m, k)


print(permutation(2, 1, [[1, 2]]))
print(permutation(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]))
print(permutation(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]))

