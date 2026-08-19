import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {

        // Put all numbers into a HashSet.
        // This removes duplicates and allows O(1) average lookup.
        Set<Integer> numSet = new HashSet<>();

        for (int num : nums) {
            numSet.add(num);
        }

        // Keeps track of the longest consecutive sequence found
        int longestSeq = 0;

        // Check every unique number
        for (int num : numSet) {

            // If num - 1 is NOT in the set,
            // then num is the START of a consecutive sequence.
            //
            // Example:
            // [100, 4, 200, 1, 3, 2]
            // When num = 1, 0 is not in the set,
            // so 1 starts the sequence: 1, 2, 3, 4
            if (!numSet.contains(num - 1)) {

                // Start counting the current sequence
                int length = 0;

                // Keep checking for consecutive numbers:
                // num, num + 1, num + 2, ...
                while (numSet.contains(num + length)) {
                    length++;
                }

                // Update the longest sequence if this one is longer
                longestSeq = Math.max(longestSeq, length);
            }
        }

        // Return the length of the longest consecutive sequence
        return longestSeq;
    }
}