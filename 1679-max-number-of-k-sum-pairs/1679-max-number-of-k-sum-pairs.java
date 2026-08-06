class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);

        int result = 0;
        int l = 0;
        int r = nums.length - 1;
        while (l < r) {
            int current = nums[l] + nums[r];

            if (current == k) {
                l++;
                r--;
                result++;
            } else if (current < k) {
                l++;
            } else {
                r--;
            }
        }

        return result;
    }
}