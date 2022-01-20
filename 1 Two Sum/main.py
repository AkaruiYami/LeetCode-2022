def two_sum(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        t = nums[:]
        second_half = target - n
        t[i] = None
        if second_half in t:
            return [i, t.index(second_half)]
