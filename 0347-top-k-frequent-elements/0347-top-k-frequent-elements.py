class Solution(object):
    #Import the counter that automatically counts how many times a number appears 

    from collections import Counter
    def topKFrequent(self, nums, k):
        #Count the frequence of each number

        count = Counter(nums)

        #Sort the numbers by their frequence starting at the number with the highest frequence 
        #count.items : pair num count with the num
        #key=lambda x:[1] sorts using the freqeunce and not the nums 
        #reverse=True : Means highest first
        sorted_nums = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []
        #Loop k times
        for i in range(k):
            #sorted_nums[i] : gives the num and frequence
            #[0] takes just the number and not the freqeunce
            result.append(sorted_nums[i][0])

        return result