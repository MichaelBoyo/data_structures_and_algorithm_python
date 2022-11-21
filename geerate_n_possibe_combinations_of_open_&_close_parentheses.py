def generate(n):
    def rec(n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n - 1, diff + 1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n - 1, diff - 1, comb, combs)
            comb.pop()

    combs = []
    rec(2 * n, 0, [], combs)
    return combs

l = [1,2,6,12]
l2 = [12,6,2,1]
print(l ==l2)
print("the  {}  side {1} {2}".format("brign", "up", "the"))
