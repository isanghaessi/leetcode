class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int current = nums[i];
            int left = target - current;
            if (map.containsKey(left)) {
                return new int[] {i, map.get(left)};
            }

            map.put(current, i);
        }

        return null;
    }
}