class Solution:
    lookup = {
        "2": list("abc"),
        "3": list("def"),
        "4": list("ghi"),
        "5": list("jkl"),
        "6": list("mno"),
        "7": list("pqrs"),
        "8": list("tuv"),
        "9": list("wxyz"),
    }

    def combine(self, l1, l2):
        return [a + b for a in l1 for b in l2]

    def letterCombinations(self, digits: str) -> list[str]:

        if digits == "":
            return []

        if len(digits) == 1:
            return self.lookup[digits]

        r = self.combine(self.lookup[digits[0]], self.letterCombinations(digits[1:]))

        return r

    def letterCombinations2(self, digits: str) -> list[str]:
        if digits == "":
            return []

        r = [""]
        for digit in digits:
            r = [a + b for a in r for b in self.lookup[digit]]
        return r


a = Solution()
r = a.letterCombinations("23")
r2 = a.letterCombinations2("23")
print(r)
print(r2)
