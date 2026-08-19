import java.util.*;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {

        // Length of the temperatures array
        int n = temperatures.length;

        // answer[i] = number of days we need to wait
        // for a warmer temperature.
        // Defaults to 0 if there is no warmer day.
        int[] answer = new int[n];

        // Stack stores the INDEX of previous days.
        // We use a stack so we can quickly find
        // the previous colder temperatures.
        Stack<Integer> stack = new Stack<>();

        // Go through each temperature
        for (int i = 0; i < n; i++) {

            // While the current temperature is warmer
            // than the temperature at the index on top
            // of the stack...
            while (!stack.isEmpty()
                    && temperatures[i] > temperatures[stack.peek()]) {

                // Remove the previous colder day
                int prev = stack.pop();

                // Calculate how many days we waited
                // from prev to the current day i
                answer[prev] = i - prev;
            }

            // Add the current day's index to the stack
            stack.push(i);
        }

        // Any indices still in the stack never found
        // a warmer temperature, so their answer stays 0.
        return answer;
    }
}