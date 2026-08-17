class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count the frequency of each number
        HashMap<Integer, Integer> count = new HashMap<>();

        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Sort the entries by frequency, highest first
        List<Map.Entry<Integer, Integer>> sortedNums =
                new ArrayList<>(count.entrySet());

        sortedNums.sort((a, b) -> b.getValue() - a.getValue());

        // Store the k most frequent elements
        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = sortedNums.get(i).getKey();
        }

        return result;
    }
}