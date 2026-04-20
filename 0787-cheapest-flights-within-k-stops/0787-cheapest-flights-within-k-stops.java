class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] result = new int[n];
        Arrays.fill(result, -1);
        result[src] = 0;

        for (int i = 0; i < k + 1; i++) {
            int[] newResult = Arrays.copyOfRange(result, 0, result.length);

            for (int[] flight: flights) {
                int from = flight[0];
                int to = flight[1];
                int time = flight[2];

                if (result[from] < 0) {
                    continue;
                }

                newResult[to] = Arrays.stream(new int[] {result[to], newResult[to], result[from] + time})
                    .filter((a) -> a >= 0)
                    .min()
                    .getAsInt();
            }

            result = newResult;
        }

        return result[dst];
    }
}