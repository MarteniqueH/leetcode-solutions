class Solution:
    def evalRPN(self, tokens):
        #create a stack to store int values 
        stack = []
        #loop through tokens one token at a time 
        for token in tokens:
            #if the token is addition
            if token == "+":
                #The most recently added number to the stack is the right operand 
                b = stack.pop()
                #The number next in the stack is the left operand 
                a = stack.pop()
                #add the numbers together and add back to the end of the stack 
                stack.append(a + b)
            #if the token is subtraction 
            elif token == "-":
                #the first value popped is the right operand 
                b = stack.pop()
                #the second value popped is the left operand 
                a = stack.pop()
                #subract the ints and append the result back to the end of the stack 
                stack.append(a - b)



            #if the token is multiplication
            elif token == "*":
                #the first value popped is the right operand 
                b = stack.pop()
                #the second value popped is the left operand 
                a = stack.pop()
                #mutiply values and append results to end of stack
                stack.append(a * b)

            #if the token is division 
            elif token == "/":
                #The first value popped goes on the right operand 
                b = stack.pop()
                #the second value poppe goes on the left
                a = stack.pop()

                # Truncate toward zero
                #maually apply the correct sign (so if one is negative the answer is negative)
                result = abs(a) // abs(b)
                #checks if the signs of the two values differ both neg or pos of opposite
                if (a < 0) != (b < 0):
                    result = -result

                #append the results back into the stack
                stack.append(result)

            else:
                #if the token is not an operator but an int just automatically add it to the stack 
                stack.append(int(token))
                
        #return the final value 
        return stack.pop()