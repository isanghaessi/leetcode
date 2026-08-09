class Solution {
    public int longestOnes(int[] nums, int k) {
        int l = 0;
        int r = 0;
        int result = 0;
        while (r < nums.length) {
            if (nums[r] == 0) {
                k--;
            }
            while (k < 0) {
                if (nums[l] == 0) {
                    k++;
                }
                l++;
            }

            result = Math.max(result, r - l + 1);
            r++;
        }

        return result;
    }
}