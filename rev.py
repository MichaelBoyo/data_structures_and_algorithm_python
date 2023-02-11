from collections import defaultdict


def reverseString(text):
    index = -1
    d = defaultdict(int)
    for i in range(len(text) - 1, int(len(text) / 2), -1):
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


string = "ab-cd"
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))