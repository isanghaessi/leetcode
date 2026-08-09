class Solution {
    public int longestSubarray(int[] nums) {
        int dc = 0;
        int l = 0;
        int r = 0;
        int result = 0;
        while (r < nums.length) {
            if (nums[r] == 0) {
                dc++;
            }
            while (dc > 1) {
                if (nums[l] == 0) {
                    dc--;
                }
                l++;
            }

            result = Math.max(result, r - l);
            r++;
        }

        return result;
    }
}