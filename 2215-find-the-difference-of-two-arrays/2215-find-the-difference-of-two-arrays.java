class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> result = new ArrayList<>();

        Set<Integer> ns1 = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            ns1.add(nums1[i]);
        }

        Set<Integer> ns2 = new HashSet<>();
        for (int i = 0; i < nums2.length; i++) {
            ns2.add(nums2[i]);
        }

        Set<Integer> result1 = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            if (!ns2.contains(nums1[i])) {
                result1.add(nums1[i]);
            }
        }
        result.add(result1.stream().toList());

        Set<Integer> result2 = new HashSet<>();
        for (int i = 0; i < nums2.length; i++) {
            if (!ns1.contains(nums2[i])) {
                result2.add(nums2[i]);
            }
        }
        result.add(result2.stream().toList());

        return result;
    }
}