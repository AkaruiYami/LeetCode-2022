class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if s == "":
            return 0

        r = 0
        sign = None
        if s[0] in ["-", "+"]:
            sign = s[0]
            s = s[1::]

        for _s in s:
            if _s.isdecimal():
                r *= 10
                r += int(_s)
            else:
                break

        if sign == "-":
            r = -r

        return max(pow(-2, 31), min(pow(2, 31) - 1, r))


a = Solution()
print(a.myAtoi("words and 987"))
print(a.myAtoi(" "))
