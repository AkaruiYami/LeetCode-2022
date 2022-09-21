class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        start = 0
        end = n - 1
        smallest_gap = float("Inf")
        while start < end:
            l = start + 1
            r = end - 1
            curr_smallest_gap = float("Inf")
            while l <= r:
                m = (l + r) // 2
                three_sum = nums[start] + nums[m] + nums[end]

                if three_sum == target:
                    return three_sum

                gap = abs(three_sum - target)
                if gap < abs(curr_smallest_gap - target):
                    curr_smallest_gap = three_sum

                if three_sum > target:
                    r = m - 1
                else:
                    l = m + 1

            gap = abs(curr_smallest_gap - target)
            if gap < abs(smallest_gap - target):
                smallest_gap = curr_smallest_gap

            if curr_smallest_gap > target:
                end -= 1
            else:
                start += 1

        return smallest_gap
