class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> timeMap = new HashMap<>();
        for (int[] time: times) {
            timeMap.putIfAbsent(time[0], new ArrayList<>());
            timeMap.get(time[0]).add(new int[] {time[1], time[2]});
        }

        int[] result = new int[n + 1];
        Arrays.fill(result, -1);
        result[0] = 0;
        result[k] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[] {k, 0});
        while (pq.size() > 0) {
            int[] current = pq.poll();
            int node = current[0];
            int time = current[1];

            if (result[node] > 0) {
                continue;
            }

            result[node] = time;

            if (!timeMap.containsKey(node)) {
                continue;
            }

            for (int[] toGo: timeMap.get(node)) {
                pq.offer(new int[] {toGo[0], time + toGo[1]});
            }
        }

        int answer = result[0];
        for(int res: result) {
            if (res < 0) {
                return -1;
            }

            answer = Math.max(answer, res);
        }

        return answer;
    }
}