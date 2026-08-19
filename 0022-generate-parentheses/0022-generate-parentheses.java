import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {

        // Stores all valid combinations
        List<String> answer = new ArrayList<>();

        // Temporary list used to build the current combination
        List<Character> result = new ArrayList<>();

        // Start backtracking with 0 open and 0 close parentheses
        backtrack(0, 0, n, result, answer);

        return answer;
    }

    private void backtrack(
        int openCount,
        int closeCount,
        int n,
        List<Character> result,
        List<String> answer
    ) {

        // If we have used n opening AND n closing parentheses,
        // we have created a complete valid combination.
        if (openCount == n && closeCount == n) {

            // Convert the characters into a String
            StringBuilder sb = new StringBuilder();

            for (char c : result) {
                sb.append(c);
            }

            answer.add(sb.toString());

            return;
        }

        // We can add an opening parenthesis as long as
        // we haven't used all n opening parentheses.
        if (openCount < n) {
            result.add('(');

            // Recursively continue building the combination
            backtrack(
                openCount + 1,
                closeCount,
                n,
                result,
                answer
            );

            // Remove the '(' so we can try another possibility.
            // This is the "backtrack" part.
            result.remove(result.size() - 1);
        }

        // We can only add a closing parenthesis if there
        // are currently more '(' than ')' .
        //
        // This prevents invalid combinations like:
        // ")("
        // "())("
        if (closeCount < openCount) {
            result.add(')');

            // Recursively continue building the combination
            backtrack(
                openCount,
                closeCount + 1,
                n,
                result,
                answer
            );

            // Remove the ')' to backtrack
            result.remove(result.size() - 1);
        }
    }
}