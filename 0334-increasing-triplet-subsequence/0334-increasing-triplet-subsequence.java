import java.util.*;

class Solution {
    public boolean increasingTriplet(int[] nums) {
        int[] mins = new int[nums.length];
        int[] maxs = new int[nums.length];
        mins[0] = nums[0];
        maxs[nums.length - 1] = nums[nums.length - 1];
        for (int i = 1; i < nums.length; i++) {
            mins[i] = Math.min(mins[i - 1], nums[i]);
            maxs[nums.length - 1 - i] = Math.max(maxs[nums.length - i], nums[nums.length - 1 - i]);
        }

        for (int i = 0; i < nums.length; i++) {
            if (mins[i] < nums[i] && nums[i] < maxs[i]) {
                return true;
            }
        }

        return false;
    }
}