
class Solution {
    public int lengthOfLastWord(String s) {
        String reversed = new StringBuilder(s).reverse().toString();

        int count = 0;

        for (char c : reversed.toCharArray()) {
            if (c == ' ' && count == 0) {
                continue;
            }

            if (c == ' ') {
                break;
            }

            count++;
        }

        return count;
    }
}