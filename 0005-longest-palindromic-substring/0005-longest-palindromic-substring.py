class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        start = 0
        max_length = 1


        def center_expander(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1

            return right - left - 1


        for i in range(len(s)):
            odd_length = center_expander(i,i)

            even_length = center_expander(i,i+1)


            current_length = max(even_length,odd_length)

            if current_length > max_length:
                max_length = current_length

                start = i - (current_length - 1) // 2


        return s[start:start + max_length]