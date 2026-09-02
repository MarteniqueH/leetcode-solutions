class Solution(object):
    def maxArea(self, height):
        # Start with two pointers:
        # left points to the first element
        # right points to the last element
        left = 0
        right = len(height) - 1

        # Keep track of the largest area found so far
        max_area = 0

        # Continue until the two pointers meet
        while left < right:

            # The width is the distance between the two pointers
            width = right - left

            # The container's height is limited by the shorter line
            min_height = min(height[left], height[right])

            # Calculate the area of water that can fit
            # Area = width × height
            area = width * min_height

            # Update max_area if the current area is larger
            max_area = max(max_area, area)

            # Move the pointer with the shorter height.
            # Why? Moving the taller pointer cannot increase
            # the height because the shorter side is still the limit.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the largest container area we found
        return max_area
            
        