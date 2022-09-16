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


a = Solution()
print(a.romanToInt("MCMXCIV"))
