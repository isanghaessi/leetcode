import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] forward = new int[nums.length];
        forward[0] = 1;
        int[] reverse = new int[nums.length];
        reverse[nums.length - 1] = 1;
        for (int i = 0; i < forward.length - 1; i++) {
            forward[i + 1] = forward[i] * nums[i];
            reverse[nums.length - i - 2] = reverse[nums.length - i - 1] *  nums[nums.length - i - 1];
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < forward.length; i++) {
            result[i] = forward[i] * reverse[i];
        }

        return result;
    }
}