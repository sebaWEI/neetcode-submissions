from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break                      # 已排序，后面都 > 0，三数和不可能为 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue                   # 跳过重复的 i
            l, r = i + 1, n - 1
            target = -nums[i]
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1             # 跳过重复的 l
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1             # 跳过重复的 r
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res