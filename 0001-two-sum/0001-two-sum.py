class Solution(object):
    def twoSum(self, nums, target): 
          # This dictionary will store numbers we have already seen
        # Key = number, Value = index of that number
        seen_numbers = {}

        # Go through the list with both index and value
        for i, current_num in enumerate(nums):

            # Find what number we need to reach the target
            complement = target - current_num

            # Check if that needed number was already seen
            if complement in seen_numbers:
                # If yes, return the index of the old number and current index
                return [seen_numbers[complement], i]

            # Otherwise, store the current number with its index
            seen_numbers[current_num] = i