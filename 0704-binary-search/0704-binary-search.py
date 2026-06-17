class Solution(object):
    def search(self, nums, target):
        for num in nums:
            if num == target:
                return nums.index(target)
        return -1
        