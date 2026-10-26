
class Solution {
    public String longestCommonPrefix(String[] strs) {

        // If the array has no words, return an empty string.
        if (strs.length == 0) {
            return "";
        }

        // Start by assuming the FIRST word is the longest
        // possible common prefix.
        // We will shorten it if it doesn't match the other words.
        String testString = strs[0];

        //  Loop through the array, starting at index 1.
        // We skip index 0 because testString already comes from there.
        for (int i = 1; i < strs.length; i++) {

            // Check whether testString appears at the
            // VERY BEGINNING of the current word.
            // indexOf() returns 0 if it starts at the beginning.
            // If it returns anything else, we need to shorten testString.
            while (strs[i].indexOf(testString) != 0) {

                //  Remove the LAST character from testString.
                // Example: "flower" becomes "flowe".
                testString = testString.substring(
                    0, testString.length() - 1
                );

                // Step 6: If testString becomes empty, there is
                // no common prefix, so return an empty string.
                if (testString.isEmpty()) {
                    return "";
                }
            }

            // Step 7: Once the while loop ends, testString is a prefix
            // of the current word. Move on to the next word.
        }

        // Step 8: Return the prefix that matches every word.
        return testString;
    }
}
