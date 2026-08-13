class Solution(object):
    def generateParenthesis(self, n):
        """
        - add ( when openCount < n 
        - add ) when closedCount < openCount
        - valid if openCount == closedCount == n
        """

        # hold parentheses 
        stack = []
        
        # list of valid parentheses combinations 
        result = []

        # function passes in open n and closed n 
        def backtrack(openCount, closeCount):

            # base case 
            # if open n == close n == n
            if openCount == closeCount == n:
                # take all characters in a string 
                # take all characters in the stack and join them into an empty string and append to result list 
                result.append("".join(stack))

                # return base case 
                return

            # check if open count is less than end 
            # add just an open parenthesis to stack
            if openCount < n:
                stack.append("(")

                # recursively continue backtrack by incrementing open count by one and leave closed the same 
                backtrack(openCount + 1, closeCount)

                # pop the character just added to the stack 
                stack.pop()

            # make sure close count is less than the open count 
            if closeCount < openCount:
                # append the closing parenthesis to the stack
                stack.append(")")

                # call recursive backtrack and increment closing count by 1 and leave open the same 
                backtrack(openCount, closeCount + 1)

                # update stack by popping the character that was just added 
                stack.pop()

        # call backtrack function and start both open and closed as 0, 0
        backtrack(0, 0)

        # return results 
        return result