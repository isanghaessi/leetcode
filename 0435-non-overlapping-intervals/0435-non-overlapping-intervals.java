class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

        int result = 0;

        int previous = 0;
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < intervals[previous][1]) {
                result++;
            } else {
                previous = i;
            }
        }

        return result;
    }
}