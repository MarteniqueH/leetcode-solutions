class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count = {0: 1}

        current_sum = 0
        result = 0

        for num in nums:
            # Add the current number to our running prefix sum
            current_sum += num

            # If we've previously seen (current_sum - k),
            # every occurrence represents a subarray ending here
            # whose sum is exactly k.
            result += prefix_count.get(current_sum - k, 0)

            # Record this prefix sum for future subarrays
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return result

