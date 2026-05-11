class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        number_of_different_unit = len(num_set)
        if number_of_different_unit < len(nums):
            return True
        return False
