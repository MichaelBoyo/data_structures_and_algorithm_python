def gibonacci(n: int, x: int, y: int) -> int:
    if n == 0:
        return x
    if n == 1:
        return y
    if n % 2 == 1:
        return x
    return gibonacci(n - y, x, y)

