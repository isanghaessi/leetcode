class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int[] result = new int[n + 1];
        Arrays.fill(result, Integer.MAX_VALUE);
        result[0] = 0;
        result[k] = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int[] time: times) {
                int from = time[0];
                int to = time[1];
                int spent = time[2];

                if (result[from] == Integer.MAX_VALUE) {
                    continue;
                }

                int newTime = result[from] + spent;
                if (result[to] > newTime) {
                    result[to] = newTime;
                }
            }
        }

        int answer = 0;
        for (int res: result) {
            if (res == Integer.MAX_VALUE) {
                return - 1;
            }

            answer = Math.max(answer, res);
        }

        return answer;
    }
}