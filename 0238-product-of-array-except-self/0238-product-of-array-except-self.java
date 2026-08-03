import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] forward = new int[nums.length];
        forward[0] = 1;
        for (int i = 0; i < forward.length - 1; i++) {
            forward[i + 1] = forward[i] * nums[i];
        }

        int[] reverse = new int[nums.length];
        reverse[nums.length - 1] = 1;
        for (int i = reverse.length - 1; i >= 1; i--) {
            reverse[i - 1] = reverse[i] *  nums[i];
        }

        int[] result = new int[nums.length];
        Arrays.fill(result, 1);
        for (int i = 0; i < forward.length; i++) {
            result[i] *= forward[i] * reverse[i];
        }

        return result;
    }
}