class Solution {
    public int[] twoSum(int[] nums, int target) {
        // This map will store numbers we have already seen
        // Key = number, Value = index of that number
        HashMap<Integer, Integer> seenNumbers = new HashMap<>();

        // Go through the array with index and value
        for (int i = 0; i < nums.length; i++) {
            int currentNum = nums[i];

            // Find what number we need to reach the target
            int complement = target - currentNum;

            // Check if that needed number was already seen
            if (seenNumbers.containsKey(complement)) {
                // If yes, return the old index and current index
                return new int[] { seenNumbers.get(complement), i };
            }

            // Otherwise, store the current number with its index
            seenNumbers.put(currentNum, i);
        }

        // No solution found
        return new int[] {};
    }
}