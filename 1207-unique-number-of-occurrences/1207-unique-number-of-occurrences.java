class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Set<Integer> counts = new HashSet<>();

        for (int i = -1000; i <= 1000; i++) {
            int count = 0;
            
            for (int j = 0; j < arr.length; j++) {
                if (arr[j] == i) {
                    count++;
                }
            }

            if (count == 0) {
                continue;
            }

            if (counts.contains(count)) {
                return false;
            }

            counts.add(count);
        }

        return true;
    }
}