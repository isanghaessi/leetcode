class Solution {
    public int largestAltitude(int[] gain) {
        int[] gainDiff = new int[gain.length + 1];
        int result = 0;

        for (int i = 0; i < gain.length; i++) {
            int diff = gainDiff[i] + gain[i];
            gainDiff[i + 1] = diff;

            result = Math.max(result, diff);
        }

        return result;
    }
}