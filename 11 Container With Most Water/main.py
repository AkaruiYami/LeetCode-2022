class Solution:
    def maxArea(self, height: list[int]) -> int:
        mx_vol = -float("inf")
        l, r = 0, len(height) - 1
        while r > l:
            h = min(height[l], height[r])
            d = r - l
            mx_vol = max(mx_vol, h * d)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return mx_vol

    def maxAreaSlow(self, height: list[int]) -> int:
        n = len(height)
        if n == 2:
            return height[0] * height[1]
        mx_vol = -float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                h = min(height[i], height[j])
                d = j - i
                print(i, j, h, d)
                mx_vol = max(mx_vol, h * d)
        return mx_vol


a = Solution()
print(a.maxArea([4, 3, 2, 1, 4]))
