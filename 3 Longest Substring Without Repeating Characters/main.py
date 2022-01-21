def solution(s: str):
    if len(s) <= 1:
        return len(s)

    tmp_s = ""
    max_len = 0

    for c in s:
        if c in tmp_s:
            tmp_s = tmp_s[tmp_s.index(c) + 1 :]
        tmp_s += c
        max_len = max(len(tmp_s), max_len)
    return max_len


test_s = ["abcabcbb", "bbbb", "pwwkew"]

for t in test_s:
    print(solution(t))
