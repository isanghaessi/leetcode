class Solution {
    public boolean canJump(int[] nums) {
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] > 0) {
                continue;
            }

            boolean check = false;

            int j = i;
            while (j >= 0) {
                int minimal = i - j + 1;

                if (j + minimal >= nums.length) {
                    check = true;
                    break;
                }

                if (nums[j] >= minimal) {
                    check = true;
                    break;
                }

                j--;
            }

            if (!check) {
                return false;
            }
        }

        return true;
    }
}