class Solution(object):
    def countSubstrings(self, s):
        def center_expander(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count = 0 

                count += 1
                left -= 1
                right += 1

                

            return count 

        total = 0
        for i in range(len(s)):
            total += center_expander(i,i)

            total += center_expander(i,i+1)

            

        return total 
        