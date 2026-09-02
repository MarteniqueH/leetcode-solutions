class Solution:
    def threeSum(self, nums):
        result = []

        # Step 1: Sort the array.
        # Sorting allows us to use the two-pointer technique
        # and makes it easier to avoid duplicate triplets.
        nums.sort()

        n = len(nums)

        # Step 2: Fix the first number of the triplet.
        for i in range(n - 2):

            # Since the array is sorted, if nums[i] > 0,
            # all numbers after it are also positive.
            # Therefore, we cannot possibly get a sum of 0.
            if nums[i] > 0:
                break

            # Skip duplicate values for the first number.
            # Example: [-1, -1, 0, 1]
            # We only need to process -1 once.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Use two pointers for the other
            # two numbers.
            left = i + 1
            right = n - 1

            while left < right:

                # Calculate the sum of the three numbers.
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # We found a valid triplet.
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    # Move both pointers to look for
                    # another possible triplet.
                    left += 1
                    right -= 1

                    # Skip duplicate values on the left.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on the right.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # The sum is too small.
                    # Because the array is sorted, moving
                    # left forward increases the sum.
                    left += 1

                else:
                    # The sum is too large.
                    # Moving right backward decreases the sum.
                    right -= 1

        return result


       



        