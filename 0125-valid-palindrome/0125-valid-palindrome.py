class Solution(object):
    
    def isPalindrome(self, s):
        # Start the left pointer at the beginning of the string.
        left = 0

        # Start the right pointer at the end of the string.
        right = len(s) - 1

        # Keep checking characters while the pointers have not crossed.
        while left < right:

            # Move the left pointer forward until we find a letter or number.
            while left < right and not self.alphaNum(s[left]):
                left += 1

            # Move the right pointer backward until we find a letter or number.
            while left < right and not self.alphaNum(s[right]):
                right -= 1

            # Compare the characters without caring about uppercase/lowercase.
            if s[left].lower() != s[right].lower():
                # If the characters are different, the string is NOT a palindrome.
                return False

            # Move both pointers toward the center.
            left += 1
            right -= 1

        # If we made it through the entire string, it is a palindrome.
        return True

    def alphaNum(self, c):
        # Return True if c is an uppercase letter.
        if ord("A") <= ord(c) <= ord("Z"):
            return True

        # Return True if c is a lowercase letter.
        if ord("a") <= ord(c) <= ord("z"):
            return True

        # Return True if c is a number from 0 through 9.
        if ord("0") <= ord(c) <= ord("9"):
            return True

        # If c is not a letter or number, return False.
        return False



        