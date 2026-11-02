class Solution {
    public int[] sortArray(int[] nums) {

        int arrayLength = nums.length;

        if(arrayLength < 2) {
            return nums;
        }

        int mid = arrayLength / 2;

        int[] leftHalf = new int[mid];
        int[] rightHalf = new int[arrayLength - mid];

        for(int i = 0; i < mid; i++) {
            leftHalf[i] = nums[i];
        }

        for(int i = mid; i < arrayLength; i++) {
            rightHalf[i - mid] = nums[i];
        }

        // Recursively sort both halves
        leftHalf = sortArray(leftHalf);
        rightHalf = sortArray(rightHalf);

        // Merge the two sorted halves
        int i = 0;
        int j = 0;
        int k = 0;

        while(i < leftHalf.length && j < rightHalf.length) {

            if(leftHalf[i] <= rightHalf[j]) {
                nums[k] = leftHalf[i];
                i++;
            } else {
                nums[k] = rightHalf[j];
                j++;
            }

            k++;
        }

        // Copy remaining elements
        while(i < leftHalf.length) {
            nums[k] = leftHalf[i];
            i++;
            k++;
        }

        while(j < rightHalf.length) {
            nums[k] = rightHalf[j];
            j++;
            k++;
        }

        return nums;
    }
}