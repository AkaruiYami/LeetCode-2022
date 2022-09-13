import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.compile(f"^{p}$")
        return re.match(p, s)

