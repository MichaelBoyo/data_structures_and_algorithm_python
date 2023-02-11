def calPoints(ops) -> int:
    record = []
    for i in ops:
        if i.isnumeric():
            record.append(int(i))
        elif i == "C":
            record = record [:-1]
        elif i == "D":
            val = sum([a * 2 for a in record])
            record.append(val)
        elif i == "+":
            record.append(sum(record))
    return sum(record)


if __name__ == "__main__":
    line = input()
    ops = line.strip().split()

    print(calPoints(ops))