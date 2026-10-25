
import java.util.Arrays;

class Solution {

    // Main method called by LeetCode.
    public long maximumCoins(int[][] coins, int k) {

        // Sort intervals by their left endpoints.
        Arrays.sort(coins, (a, b) -> Integer.compare(a[0], b[0]));

        // Store the number of intervals.
        int n = coins.length;

        // prefix[i] stores the coins in intervals 0 through i - 1.
        long[] prefix = new long[n + 1];

        // Build the prefix sum array.
        for (int i = 0; i < n; i++) {

            // Calculate the number of bags in this interval.
            long length = (long) coins[i][1] - coins[i][0] + 1;

            // Calculate the total coins in this interval.
            long intervalCoins = length * coins[i][2];

            // Add the interval's coins to the running prefix sum.
            prefix[i + 1] = prefix[i] + intervalCoins;
        }

        // Store the maximum coins found.
        long answer = 0;

        // Try a window starting at every interval's left endpoint.
        for (int i = 0; i < n; i++) {

            // Set the left edge of the window.
            long left = coins[i][0];

            // Calculate the inclusive right edge of the window.
            long right = left + k - 1;

            // Calculate the coins inside this window.
            long total = getCoins(coins, prefix, left, right);

            // Keep the largest result.
            answer = Math.max(answer, total);
        }

        // Try a window ending at every interval's right endpoint.
        for (int i = 0; i < n; i++) {

            // Set the right edge of the window.
            long right = coins[i][1];

            // Calculate the inclusive left edge of the window.
            long left = right - k + 1;

            // Calculate the coins inside this window.
            long total = getCoins(coins, prefix, left, right);

            // Keep the largest result.
            answer = Math.max(answer, total);
        }

        // Return the maximum coins obtainable.
        return answer;
    }

    // Calculate the coins inside a window using prefix sums.
    private long getCoins(
            int[][] coins, long[] prefix, long left, long right) {

        // Store the number of intervals.
        int n = coins.length;

        // Find the first interval whose right endpoint is at least left.
        int low = 0;

        // Set the upper limit for binary search.
        int high = n;

        // Search for the first interval that may overlap the window.
        while (low < high) {

            // Calculate the middle index.
            int mid = low + (high - low) / 2;

            // Check whether this interval ends before the window.
            if (coins[mid][1] < left) {

                // Skip this interval and all earlier intervals.
                low = mid + 1;

            } else {

                // Search the left half for an earlier overlapping interval.
                high = mid;
            }
        }

        // Save the first potentially overlapping interval.
        int first = low;

        // Reset the lower search boundary.
        low = 0;

        // Reset the upper search boundary.
        high = n;

        // Find the first interval whose left endpoint is greater than right.
        while (low < high) {

            // Calculate the middle index.
            int mid = low + (high - low) / 2;

            // Check whether this interval starts within the window.
            if (coins[mid][0] <= right) {

                // Search farther to the right.
                low = mid + 1;

            } else {

                // Search the left half.
                high = mid;
            }
        }

        // Save the index immediately after the last overlapping interval.
        int end = low;

        // Return zero if no interval overlaps the window.
        if (first >= end) {
            return 0;
        }

        // Handle a window that overlaps only one interval.
        if (first == end - 1) {

            // Find the first covered bag.
            long overlapLeft = Math.max(left, (long) coins[first][0]);

            // Find the last covered bag.
            long overlapRight = Math.min(right, (long) coins[first][1]);

            // Calculate the coins from the overlapping bags.
            return Math.max(0L, overlapRight - overlapLeft + 1)
                    * coins[first][2];
        }

        // Count the coins from the first partially covered interval.
        long total = ((long) coins[first][1]
                - Math.max(left, (long) coins[first][0]) + 1)
                * coins[first][2];

        // Add the coins from all complete intervals between the endpoints.
        total += prefix[end - 1] - prefix[first + 1];

        // Count the coins from the last partially covered interval.
        total += (Math.min(right, (long) coins[end - 1][1])
                - coins[end - 1][0] + 1)
                * coins[end - 1][2];

        // Return the total coins in the window.
        return total;
    }
}