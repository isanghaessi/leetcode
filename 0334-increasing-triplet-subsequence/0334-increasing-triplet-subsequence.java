class Solution {
    public boolean increasingTriplet(int[] nums) {
        int[] mins = new int[nums.length];
        int cm = nums[0];
        for (int i = 0; i < nums.length; i++) {
            mins[i] = Math.min(cm, nums[i]);
            cm = mins[i];
        }

        int[] maxs = new int[nums.length];
        cm = nums[nums.length - 1];
        for (int i = nums.length - 1; i >= 0; i--) {
            maxs[i] = Math.max(cm, nums[i]);
            cm = maxs[i];
        }

        for (int i = 0; i < nums.length; i++) {
            if (mins[i] < nums[i] && nums[i] < maxs[i]) {
                return true;
            }
        }

        return false;
    }
}