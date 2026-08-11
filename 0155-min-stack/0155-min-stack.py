class MinStack(object):

    def __init__(self):
        #main stack to store input values
        self.stack = []
        #stack that stores the minimum value
        self.minStack = []
        

    def push(self, value):
        #pushes input value to main stack
        self.stack.append(value)
        #if the minStack is empty the new value becomes min
        #if min stack is not empty compare the current value to the top value of min stack to find the smaller value 
        if self.minStack:
            value = min(value, self.minStack[-1])
        self.minStack.append(value)
        

    def pop(self):
        #remove top value from stack and min stack
        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        #return the top value of main stack 
        return self.stack[-1]
        

    def getMin(self):
        #return top value of min stack
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()