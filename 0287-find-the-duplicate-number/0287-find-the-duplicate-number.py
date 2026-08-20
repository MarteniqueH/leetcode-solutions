class Solution(object):
    from collections import Counter

    def findDuplicate(self, nums):

        # Count how many times each number appears in nums
        # Example: [1, 3, 4, 2, 2]
        # becomes: {1: 1, 3: 1, 4: 1, 2: 2}
        count = Counter(nums)

        # count.items() gives us (number, frequency) pairs
        # Example: [(1, 1), (3, 1), (4, 1), (2, 2)]
        #
        # key=lambda x: x[1] means:
        # sort based on the frequency (the second value)
        #
        # reverse=True means:
        # put the highest frequency first
        sorted_nums = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # sorted_nums[0] gets the first tuple
        # Example: (2, 2)
        #
        # sorted_nums[0][0] gets the number from that tuple
        # Example: 2
        #
        # So we return the number that appeared most often
        return sorted_nums[0][0]