class Solution {
    public int singleNumber(int[] nums) {
        Set<Integer> result = new HashSet<>();

        for (int num: nums) {
            if (result.contains(num)) {
                result.remove(num);
            } else {
                result.add(num);
            }
        }

        return new ArrayList<>(result).get(0);
    }
}