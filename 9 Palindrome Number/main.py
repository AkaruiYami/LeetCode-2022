class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        if 0 < x < 10:
            return True

        y = 0
        temp = x
        while temp != 0:
            y = y * 10 + (temp % 10)
            temp //= 10

        return x == y

    def isPalindromeFast(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        y = "".join(reversed(str(x)))
        return x == int(y)


a = Solution()
print(a.isPalindrome(-121))
print(a.isPalindromeFast(-121))
