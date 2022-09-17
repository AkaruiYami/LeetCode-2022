class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        r = ""
        s1 = strs.pop()
        for i in range(1, len(s1) + 1):
            lookup = [False for _ in range(len(strs))]

            for idx, s in enumerate(strs):
                if s.startswith(s1[:i]):
                    lookup[idx] = True
                else:
                    break

            if all(lookup):
                r = s1[:i]
            else:
                break

        return r

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        s = strs[0]
        r = ""
        for c in s:
            if strs[-1].startswith(r + c):
                r += c
            else:
                break
        return r


a = Solution()
r = a.longestCommonPrefix(["flower", "flow", "flight"])
r = a.longestCommonPrefix2(["flower", "flow", "flight"])
print(r)
