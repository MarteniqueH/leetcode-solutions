class Solution {
    public int searchInsert(int[] nums, int target) {
        // set the left pointer at the begining of the array
        int left = 0;
        // set the right pointer at the end of the array
        int right = nums.length - 1;
        //while the left pointer has not passed the right pointer and is not in the same position as the right pointer continue 
        while (left <= right) {
            // Determine the mid of the array 
            // right - left is the distance between two pointers 
            // / 2 finds the half of the distance 
            //Starts at the left pointer and moves half way toward the right pointer
            int mid = left + (right - left) / 2;
            // if the mid point is currently equal to the target value return the index which owould be mid 
            if (nums[mid] == target) {
                return mid;

            // if the mid point is less than the target value move the left to the mid point position + one past it
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                // if the mid point value is larger than the target then move the right pointer to the mid point minus the position behind it
                right = mid - 1;
            }
        }
        //return left because all number before the left are smaller than the target and the current position of left is at a number bigger than the target so that is the exact position where the target would go
        return left;
    }
}