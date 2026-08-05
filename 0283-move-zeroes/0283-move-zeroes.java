class Solution {
    public void moveZeroes(int[] nums) {
        int zi = 0;
        while (zi < nums.length && nums[zi] != 0) {
            zi++;
        }

        while (zi < nums.length) {
            int ni = zi;
            while (ni < nums.length && nums[ni] == 0) {
                ni++;
            }

            if (ni >= nums.length) {
                break;
            }

            nums[zi] = nums[ni];
            nums[ni] = 0;

            while (zi < nums.length && nums[zi] != 0) {
                zi++;
            }
        }
    }
}