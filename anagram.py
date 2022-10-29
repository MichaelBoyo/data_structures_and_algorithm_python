from collections import Counter


def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
