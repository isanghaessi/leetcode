class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
        int count = 0;
        while (i < nums.length - count) {
            if (nums[i] == 0) {
                shift(nums, i);
                count++;
            } else {
                i++;
            }
        }
    }

    private void shift(int[] array, int offset) {
        if (offset + 1 > array.length) {
            return;
        }

        for (int i = offset; i < array.length - 1; i++) {
            array[i] = array[i + 1];
        }

        array[array.length - 1] = 0;
    }
}