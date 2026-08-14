class Solution(object):
    # Given an array of integers representing daily temperatures,
    # return an array where answer[i] is the number of days we must wait
    # after day i to get a warmer temperature.
    # If there is no warmer temperature in the future, answer[i] remains 0.
    def dailyTemperatures(self, temperatures):

        # Get the total number of temperatures in the array.
        n = len(temperatures)

        # Create the answer array and initialize every value to 0.
        # A value will be updated later if we find a warmer temperature.
        answer = [0] * n

        # The stack stores the indices of temperatures that are still
        # waiting for a warmer temperature.
        stack = []

        # Loop through each temperature using its index.
        for i in range(n):

            # While the stack is not empty AND the current temperature
            # is warmer than the temperature at the index on top of the stack,
            # we have found the warmer day for that previous temperature.
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Remove the index of the previous temperature
                # because we have now found a warmer temperature for it.
                prev = stack.pop()

                # Calculate how many days passed between the previous day
                # and the current day, then store that number in the answer.
                answer[prev] = i - prev

            # Add the current index to the stack.
            # This temperature will wait for a warmer temperature in the future.
            stack.append(i)

        # Return the completed answer array.
        return answer

        