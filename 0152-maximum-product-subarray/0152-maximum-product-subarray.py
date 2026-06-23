class Solution(object):
    def maxProduct(self, nums):
        #Initialize the best product at index 0 
        max_ending_here = nums[0]

        #Initialize the worst product at index 0 

        min_ending_here = nums[0]


        #This stores the best answer seen so fare 

        result = nums[0]

        #Start at index 1 since index 0 is already initialized
        for i in range(1,len(nums)):
            #The current number being processed 

            x = nums[i]
        #Start with a new x value 
        #Extend previous max 
        #Extend previous min
            options = (x, max_ending_here * x, min_ending_here * x)

        #Pick the best possible product ending at the index 

            max_ending_here = max(options)

        #Keep track of the worst product so fare 

            min_ending_here = min(options)

        #Update the best answer seen so far 

            result = max(result, max_ending_here)


        return result