def convert(s: str, row_num: int) -> str:
    if row_num == 1:
        return s
    
    step = 2 * (row_num - 1)
    first = s[0::step]
    last = s[row_num-1::step]

    if row_num == 2:
        return first + last

    mid = ""
    for row in range(1, row_num-1):
        for i in range(row, len(s), step):
            mid += s[i]
            if i + step - (2 * row) > len(s) - 1:
                continue
            mid += s[i + step - (2 * row)]

    return first + mid + last

if __name__ == "__main__":
    txt = "ABC"
    row_num = 3
    r = convert(txt, row_num)

    print(r)
