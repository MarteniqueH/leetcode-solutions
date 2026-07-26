class Solution:
    def twoSum(self, nums, target):
        seen_numbers = {}

        for i, current_num in enumerate(nums):
            complement = target - current_num
            if complement in seen_numbers:
                return [seen_numbers[complement], i]
            seen_numbers[current_num] = i
