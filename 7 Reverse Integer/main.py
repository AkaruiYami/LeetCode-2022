class Solution:
    def reverse(self, x: int) -> int:
        sx = str(x).removeprefix("-")
        rev_int = int("".join(reversed(sx)))
        if x < 0:
            rev_int = -rev_int

        if pow(-2, 31) <= rev_int <= pow(2, 31) - 1:
            return rev_int
        return 0


a = Solution()
print(a.reverse(123))
