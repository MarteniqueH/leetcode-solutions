class Solution(object):
    def firstStableIndex(self, nums, k):
         # Loop through every index
        for i in range(len(nums)):

            # Find the biggest value from index 0 to i
            biggest = max(nums[0:i + 1])

            # Find the smallest value from index i to the end
            smallest = min(nums[i:])

            # Calculate instability score
            instability = biggest - smallest

            # Check if this index is stable
            if instability <= k:
                return i

        # No stable index was found
        return -1