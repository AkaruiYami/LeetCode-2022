def solution(s: str):
    n = len(s)
    if n == 1:
        return s
    elif n == 2:
        return s if s[0] == s[1] else s[0]

    pairs = (i for i in range(n - 1) if s[i] == s[i + 1])
    triplets = (i for i in range(n - 2) if s[i] == s[i + 2])
    pal = s[0]

    def grow(left: int, right: int, pal: str):
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > len(pal):
                pal = s[left : right + 1]
            left -= 1
            right += 1
        return pal

    for i in pairs:
        pal = grow(i, i + 1, pal)
    for i in triplets:
        pal = grow(i, i + 2, pal)

    return pal


if __name__ == "__main__":
    s = "babad"
    print(solution(s))
