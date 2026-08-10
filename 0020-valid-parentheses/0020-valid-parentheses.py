class Solution(object):
    def isValid(self, s):
        # We use a stack to keep track of opening brackets we have seen.
        stack = []

        # This dictionary tells us which opening bracket matches each closing bracket.
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Go through each character in the string one at a time.
        for c in s:

            # If the character is in our dictionary, it means we found a closing bracket.
            if c in closeToOpen:

                # Make sure the stack is not empty and that the most recent opening bracket
                # matches the current closing bracket.
                if stack and stack[-1] == closeToOpen[c]:

                    # The brackets match, so we can remove the opening bracket from the stack.
                    stack.pop()

                # If the stack is empty or the brackets do not match, the string is invalid.
                else:
                    return False

            # If it is not a closing bracket, it must be an opening bracket,
            # so we add it to the stack and wait for its matching closing bracket.
            else:
                stack.append(c)

        # If the stack is empty, every opening bracket had a matching closing bracket.
        # If anything is left in the stack, there are unmatched opening brackets.
        return True if not stack else False




        
            

        



        