class Solution {
    public int largestAltitude(int[] gain) {
        int[] result = new int[gain.length + 1];

        for (int i = 0; i < gain.length; i++) {
            result[i + 1] = result[i] + gain[i];
        }

        return Arrays.stream(result).max().getAsInt();
    }
}