class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> counts = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            if (!counts.containsKey(arr[i])) {
                counts.put(arr[i], 0);
            }
            counts.put(arr[i], counts.get(arr[i]) + 1);
        }

        Set<Integer> seen = new HashSet<>();

        for (int count: counts.values()) {
            if (seen.contains(count)) {
                return false;
            }

            seen.add(count);
        }

        return true;
    }
}