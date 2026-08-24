class Solution(object):
    def largestRectangleArea(self, heights):
       #Finds the largest rectangular area that can be made from the histogram

            #Stores indexes of bars in increasing height order
            stack = []

            #Keeps track of the largest area found so far
            best = 0

            #Loops through every bar, plus one extra iteration to process remaining bars
            for right in range(len(heights) + 1):

                #Uses height 0 at the end so every remaining bar gets processed
                current_height = heights[right] if right < len(heights) else 0

                #Removes bars from the stack while the current bar is shorter
                #This means the removed bar can no longer extend to the right
                while stack and heights[stack[-1]] > current_height:

                    #Gets the index of the bar being removed
                    height_index = stack.pop()

                    #Gets the height of the rectangle using that bar
                    height = heights[height_index]

                    #If the stack is empty, the rectangle extends from index 0 to right - 1
                    #Otherwise, the rectangle starts after the new top of the stack
                    left = stack[-1] + 1 if stack else 0

                    #Calculates how many bars wide the rectangle can be
                    #Right is not included because the current bar is shorter
                    width = right - left

                    #Calculates the area using the removed bar as the shortest height
                    area = height * width

                    #Compares the newly calculated area with the current best
                    #and keeps whichever is larger
                    best = max(best, area)

                #Adds the current bar to the stack
                #The stack stays in increasing height order
                stack.append(right)

            #Returns the largest rectangle area found
            return best

                    