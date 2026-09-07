class Solution(object):
    def largestRectangleArea(self, heights):
        # This stack will store the INDEXES of bars.
        # We use indexes instead of heights because we need
        # to calculate the width of each rectangle.
        stack = []

        # Keep track of the largest rectangle area we have found.
        largest = 0

        # Add a 0 to the end.
        # This forces us to remove/process all remaining bars
        # from the stack when we reach the end.
        heights.append(0)

        # Go through every bar in the histogram.
        # i = index of the bar
        # h = height of the bar
        for i, h in enumerate(heights):

            # If the current bar is shorter than the bar
            # at the top of the stack, we can no longer extend
            # that taller bar to the right.
            #
            # So we remove the taller bar from the stack
            # and calculate the rectangle it could make.
            while stack and h < heights[stack[-1]]:

                # Get the height of the bar we are removing.
                height = heights[stack.pop()]

                # After popping, the bar at the top of the stack
                # tells us where the rectangle can start.
                #
                # If the stack isn't empty, stack[-1] is the
                # first smaller bar to the LEFT.
                if stack:
                    left = stack[-1]

                # If the stack is empty, there is no smaller bar
                # to the left, so we can extend all the way
                # to the beginning of the histogram.
                else:
                    left = -1

                # Calculate how many bars wide the rectangle is.
                #
                # i = first smaller bar to the RIGHT
                # left = first smaller bar to the LEFT
                #
                # We subtract 1 because neither smaller bar
                # can be included in the rectangle.
                width = i - left - 1

                # Calculate the rectangle's area:
                #
                # area = height × width
                #
                # Then compare it with the largest area we've
                # found so far.
                largest = max(largest, width * height)

            # Add the current bar's index to the stack.
            #
            # The stack keeps indexes of bars in increasing
            # height order (from bottom to top).
            stack.append(i)

        # Return the biggest rectangle area we found.
        return largest
