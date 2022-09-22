class Solution:
    def combine(self, l1, l2):
        return [a + b for a in l1 for b in l2]

    def letterCombinations(self, digits: str) -> list[str]:

        if digits == "":
            return []

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

        if len(digits) == 1:
            return lookup[digits]

        r = self.combine(lookup[digits[0]], self.letterCombinations(digits[1:]))

        return r


a = Solution()
r = a.letterCombinations("23")
print(r)
