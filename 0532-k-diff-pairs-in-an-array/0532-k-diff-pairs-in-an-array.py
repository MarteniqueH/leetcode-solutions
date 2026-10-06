class Solution(object):
    def findPairs(self, nums, k):
        # Negative k is impossible because absolute difference
        # can never be negative.
        if k < 0:
            return 0

        # Count how many times each number appears.
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        result = 0

        # k = 0 means we need the same number twice.
        if k == 0:
            for x in count:
                if count[x] >= 2:
                    result += 1

        # k > 0: look for a number that is exactly k larger.
        else:
            for x in count:
                if x + k in count:
                    result += 1

        return result
