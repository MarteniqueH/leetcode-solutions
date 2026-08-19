import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // HashMap stores:
        // key   = sorted version of the word
        // value = list of words that are anagrams
        Map<String, List<String>> result = new HashMap<>();

        // Go through every word in the input
        for (String word : strs) {

            // Convert the word into a character array
            char[] chars = word.toCharArray();

            // Sort the characters
            // Example: "eat" -> ['a', 'e', 't']
            // Anagrams will have the same sorted characters
            Arrays.sort(chars);

            // Convert the sorted characters back into a String
            // This becomes our key
            String key = new String(chars);

            // If this key doesn't exist, create a new ArrayList
            // Then add the original word to that list
            result.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        // Return only the lists of anagrams
        return new ArrayList<>(result.values());
    }
}