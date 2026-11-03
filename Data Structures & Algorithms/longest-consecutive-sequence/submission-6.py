class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_num = sorted(list(set(nums)))
        max_length = 0
        current_length = 0
        for i in range(len(sorted_num)):
            if len(sorted_num) == 1:
                return 1
            if len(sorted_num) == 0:
                return 0

            if i == len(sorted_num) - 1:
                if sorted_num[i] == sorted_num[i-1] + 1:
                    current_length += 1
                    if current_length >= max_length:
                        max_length = current_length
                        return max_length
                else:
                    if current_length >= max_length:
                        max_length = current_length
                        return max_length
            elif i == 0:
                current_length = 1
            else:
                if sorted_num[i] == sorted_num[i-1] + 1:
                    current_length += 1
                else:
                    if current_length >= max_length:
                        max_length = current_length
                        current_length = 1
                    else:
                        current_length = 1
        return max_length


        