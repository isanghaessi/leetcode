class Solution {
    public int search(int[] nums, int target) {
        int result = -1;

        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int current = nums[mid];

            if (current == target) {
                return mid;
            }

            int leftMin = nums[left];
            int rightMax = nums[right];
            if (current < target) {
                if (rightMax >= target || current > rightMax) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                if (leftMin <= target || current < leftMin) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }

        return -1;
    }
}