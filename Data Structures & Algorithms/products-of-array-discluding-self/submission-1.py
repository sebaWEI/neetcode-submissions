class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        out = [1] * n

        # 从左往右：out[i] = nums[0..i-1] 的乘积
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]

        # 从右往左：乘上 nums[i+1..n-1] 的乘积
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]

        return out


                
        
