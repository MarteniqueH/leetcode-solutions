class Solution(object):
    def rob(self, nums):

        #If their is only one house ROB IT !
        if len(nums) == 1:
            return nums[0]
        #Helper function that solves as if houses are in a straight line 
        #Solving like House Robber 1 problem
        def houseRobber(arr):
            #Represents the best profit two houses back 
            last2 = 0

            #Representes the beat profit up to the previous house
            last1 = 0

            #Loop through every house
            for money in arr:

                #At the current house the choice is to rob it or skip
                #Decide which has a larger amount of money
                current = max(last1, last2 + money)

                last2 = last1
                last1 = current

            return last1

        return max(

            #Removes the last house 
            houseRobber(nums[:-1]),

            #Removes the first house 
            houseRobber(nums[1:])
        )