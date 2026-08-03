import java.util.*;

class Solution {
    public boolean increasingTriplet(int[] nums) {
        int[] mins = Arrays.copyOfRange(nums, 0, nums.length);
        int[] maxs = Arrays.copyOfRange(nums, 0, nums.length);
        for (int i = 1; i < nums.length; i++) {
            mins[i] = Math.min(mins[i - 1], mins[i]);
            maxs[nums.length - 1 - i] = Math.max(maxs[nums.length - i], maxs[nums.length - 1 - i]);
        }

        for (int i = 0; i < nums.length; i++) {
            if (mins[i] < nums[i] && nums[i] < maxs[i]) {
                return true;
            }
        }

        return false;
    }
}