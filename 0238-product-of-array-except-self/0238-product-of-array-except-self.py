class Solution(object):
    def productExceptSelf(self, nums):

        #Store the size of the array 
        n = len(nums)

        #Create an output array
        answer = [1] * n

        #Keeps track of the product of everything to the left 

        left = 1

        #Move from left to right 
        for i in range(n):
            #Store the current left product
            answer[i] = left
            #Now multiply the current number to the future products
            left*=nums[i]
        #Compute the right values
        right = 1

        #Moving from right to left 

        for i in range(n-1, -1, -1):
            #multiple the left product already stored with the current product 

            answer[i] *= right

            #Update the running product for the next interation 
            right *=nums[i]

        return answer

