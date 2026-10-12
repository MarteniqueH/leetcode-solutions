class Solution(object):
    def minChanges(self, nums, k):
        #make the absolute difference of every mirrored pair equal
        #mirrored pair is the first number - last number = X
        #then move inward second number - second to last number = X
        #so on and so on
        #What one single number would make all of the difference between the mirroring numbers the same . All the X values the same 

        #for each pair of numbers two types of changes can occcur
            #change one number |change a - keep b| = X (vice versa too)
            #change both numbers |change a - change b| = X

        #goal is to find the pair of numbers where only one changed number is needed to get to X

        n = len(nums)

        changes = [0] * (k+2)


        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a,b)
            y = max(a,b)

            d = y - x

            limit = max(y, k - x)

            changes[0] += 1
            changes[d] -= 1
            changes[d+1] += 1
            changes[limit + 1] += 1

        answer = n
        total = 0

        for target in range(k+1):
            total += changes[target]
            answer = min(answer, total)


        return answer





