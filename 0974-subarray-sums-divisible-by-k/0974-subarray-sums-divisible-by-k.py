class Solution(object):
    def subarraysDivByK(self, nums, k):
        #What are all of the subarrays that include two numbers that have a sum divisible by k

        #input array nums and k target 
        #process find all the subarrays that all the numbers inside of the subarray added together provides a total that is divisible by k 

        #return the count of subarrays found 


        # Keep track of the running prefix sum.
        Sum = 0

        # Keep track of how many valid subarrays we have found.
        subarray_Count = 0

        # Store how many times each remainder has appeared.
        # We start with remainder 0 appearing once because an empty prefix has sum 0.
        remainder_count = {0: 1}

        # Go through every number in the array.
        for num in nums:

            # Add the current number to our running prefix sum.
            Sum += num

            # Find the remainder of the prefix sum when divided by k.
            remainder = Sum % k

            # If we have seen this remainder before,
            # each previous occurrence gives us another valid subarray.
            if remainder in remainder_count:

                # Add the number of previous occurrences of this remainder.
                subarray_Count += remainder_count[remainder]

            # Record that we have now seen this remainder one more time.
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        # Return the total number of subarrays whose sum is divisible by k.
        return subarray_Count

            