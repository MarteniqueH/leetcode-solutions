class Solution(object):
    def moveZeroes(self, nums):
        result = []
        count = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                result.append(num)

        result.extend([0] * count)

        nums[:] = result