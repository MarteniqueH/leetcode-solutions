class Solution(object):
    def longestConsecutive(self, nums):
        #Convert given list into a set for an easier way to determine if a number exist in the set
        nums_set = set(nums)
        #Stores the longest sequence currently found
        longest_seq = 0
        #loops through every number
        for n in nums_set:
            #Determining if the number is the beginning of a sequence
            #A sequence starts when the previous number does not exist
            if (n - 1) not in nums_set:
                #when found that is the start of the sequence
                length = 0

                #this keeps the count moving forward by 1
                while (n + length) in nums_set:
                    length += 1
                #Now determine if that is the biggest sequence seen so far
                longest_seq = max(length, longest_seq)

        return longest_seq

