class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        r = 0
        len_s = len(s)
        for i in range(len_s):
            if i < len_s - 1 and s[i] + s[i + 1] in d.keys():
                r += d[s[i] + s[i + 1]]
                s = s.replace(s[i] + s[i + 1], "--")
                continue
            if s[i] in d.keys():
                r += d[s[i]]
        return r

    def romanToInt2(self, s: str) -> int:
        d1 = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        d2 = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}

        for k, v in d2.items():
            s = s.replace(k, f"+{v}")

        for k, v in d1.items():
            s = s.replace(k, f"+{v}")

        return eval(s.strip("+"))

    def romanToInt3(self, s: str) -> int:
        d = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        r = 0
        for a, b in zip(s, s[1:]):
            if d[a] < d[b]:
                r -= d[a]
            else:
                r += d[a]
        return r + d[a[-1]]


a = Solution()
print(a.romanToInt("MCMXCIV"))
print(a.romanToInt2("MCMXCIV"))
