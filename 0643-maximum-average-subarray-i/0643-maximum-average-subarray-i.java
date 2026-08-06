class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double result = 0;
        double current = 0;
        for (int i = 0; i < k; i++) {
            current += nums[i];
        }
        result = current / k;

        int l = 0;
        for (int r = k; r < nums.length; r++) {
            current = current - nums[l++] + nums[r];
            result = Math.max(result, current / k);
        }

        return result;
    }
}