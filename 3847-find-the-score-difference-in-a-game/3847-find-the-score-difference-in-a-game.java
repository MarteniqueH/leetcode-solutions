
class Solution {
    public int scoreDifference(int[] nums) {

        int firstPlayer = 0;
        int secondPlayer = 0;
        int activePlayer = 0;

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] % 2 != 0) {
                activePlayer = 1 - activePlayer;
            }

            if ((i + 1) % 6 == 0) {
                activePlayer = 1 - activePlayer;
            }

            if (activePlayer == 0) {
                firstPlayer += nums[i];
            } else {
                secondPlayer += nums[i];
            }
        }

        return firstPlayer - secondPlayer;
    }
}
