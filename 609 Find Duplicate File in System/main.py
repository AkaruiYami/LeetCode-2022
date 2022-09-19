import re
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        seen_contents = defaultdict(list)
        p = re.compile(r"\s?(?P<filename>\w+\.\w+)\((?P<content>\w*)\)")
        for path in paths:
            _dir, *_files = path.split()
            for file in _files:
                m = p.match(file)
                name = m.group("filename")
                content = m.group("content")
                t = f"{_dir}/{name}"
                seen_contents[content].append(t)

        r = [g for g in seen_contents.values() if len(g) > 1]
        return r


a = Solution()
r = a.findDuplicate(
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"]
)
r = a.findDuplicate(
    [
        "root/a 1.txt(abcd) 2.txt(efsfgh)",
        "root/c 3.txt(abdfcd)",
        "root/c/d 4.txt(efggdfh)",
    ]
)
print(r)
