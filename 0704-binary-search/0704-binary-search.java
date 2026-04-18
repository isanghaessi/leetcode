class Solution {
    public int search(int[] nums, int target) {
        return _search(nums, target, 0);
    }

    int _search(int[] nums, int target, int offset) {
        if (nums == null || nums.length < 1) {
            return -1;
        }

        int mid = nums.length / 2;
        int current = nums[mid];
        
        if (current == target) {
            return offset + mid;
        } else if (current < target) {
            return _search(Arrays.copyOfRange(nums, mid + 1, nums.length), target, offset + mid + 1);
        } else {
            return _search(Arrays.copyOfRange(nums, 0, mid), target, offset);
        }
    }
}