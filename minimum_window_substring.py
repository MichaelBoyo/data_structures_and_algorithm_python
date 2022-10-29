from collections import Counter


def contains_all(freq1, freq2):
    for ch in freq2:
        if freq1[ch] < freq2[ch]:
            return False
    return True


def min_window(s, t):
    n, m = len(s), len(t)
    if m > n or m == 0:
        return ""
    fret = Counter(t)
    shortest = " " * (n + 1)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            frees = Counter(sub)
            if contains_all(frees, fret) and length < len(shortest):
                shortest = sub
    return shortest if len(shortest) <= n else ""


def min_window2(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freq = Counter(t)
    start, end = 0, n + 1
    for length in range(1, n + 1):
        frees = Counter()
        satisfied = 0
        for ch in s[:length]:
            frees[ch] += 1
            if ch in freq and frees[ch] == freq[ch]:
                satisfied += 1
        if satisfied == len(freq) and length < end - start:
            start, end = 0, length
        for i in range(1, n - length + 1):
            frees[s[i + length - 1]] += 1
            if s[i + length - 1] in freq and frees[s[i + length - 1]] == freq[s[i + length - 1]]:
                satisfied += 1
            if s[i - 1] in freq and frees[s[i - 1]] == freq[s[i - 1]]:
                satisfied -= 1
            frees[s[i - 1]] -= 1
            if satisfied == len(freq) and length < end - start:
                start, end = i, i + length
    return s[start:end] if end - start <= n else ""


def min_window1(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freq = Counter(t)
    start, end = 0, n
    satisfied = 0
    frees = Counter()
    left = 0
    for right in range(n):
        frees[s[right]] += 1
        if s[right] in freq and frees[s[right]] == freq[s[right]]:
            satisfied += 1
        if satisfied == len(freq):
            while s[left] not in freq or frees[s[left]] > freq[s[left]]:
                frees[s[left]] -= 1
                left += 1
            if right - left + 1 < end - start + 1:
                start, end = left, right
    return s[start:end + 1] if end - start + 1 <= n else ""
