class Solution {
    public int pivotIndex(int[] nums) {
        int[] left = new int[nums.length + 2];
        for (int i = 1; i < nums.length; i++) {
            left[i] = left[i - 1] + nums[i - 1];
        }
        left[nums.length] = left[nums.length - 1];

        int[] right = new int[nums.length + 2];
        for (int i = nums.length; i >= 1; i--) {
            right[i] = right[i + 1] + nums[i - 1];
        }
        right[0] = right[1];

        for (int i = 1; i <= nums.length; i++) {
            if (left[i - 1] == right[i + 1]) {
                return i - 1;
            }
        }

        return -1;
    }
}