from collections import defaultdict
from itertools import compress


class Solution:
    def threeSum1(self, nums: list[int]) -> list[list[int]]:

        res = []
        seen = set()
        t = defaultdict(list)

        for ix, x in enumerate(nums):
            for iy in range(ix + 1, len(nums)):
                t[x + nums[iy]].append([ix, iy])

        for k, v in t.items():
            if -k not in nums:
                continue

            for _v in v:
                mask = [i not in _v for i in range(len(nums))]
                tmp = list(compress(nums, mask))

                if -k not in tmp:
                    continue

                r = [nums[_v[0]], nums[_v[1]], -k]

                if frozenset(r) in seen:
                    continue
                seen.add(frozenset(r))
                res.append(r)

        return res

    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return set(res)


a = Solution()
r = a.threeSum2([-1, 0, 1, 2, -1, -4])
print(r)
