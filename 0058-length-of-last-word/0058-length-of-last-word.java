
class Solution {
    public int lengthOfLastWord(String s) {
        // reverse the string 
        String reversed = new StringBuilder(s).reverse().toString();
        // create count for charater count in last word 
        int count = 0;
        //for each charater in the reversed string 
        for (char c : reversed.toCharArray()) {
            // if the character is a space and the not characters have been counted yet 
            // if characters have been counted and we encounter another space then we have reached the end of the word
            if (c == ' ' && count == 0) {
                continue;
            }
            // if the current character is a space stop the loop completely 
            if (c == ' ') {
                break;
            }
            //increase count when it is not a space
            count++;
        }

        return count;
    }
}