class Solution(object):
    from collections import Counter
    def majorityElement(self, nums):
        #given nums 
        #return majority element

        count = Counter(nums)

       

        for num, freq in sorted(count.items()):
            if freq > len(nums) // 2:
                return num
             



        