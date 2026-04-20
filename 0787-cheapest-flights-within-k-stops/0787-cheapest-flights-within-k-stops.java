class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, List<int[]>> flightMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            flightMap.putIfAbsent(i, new ArrayList<>());
        }
        for (int[] flight: flights) {
            flightMap.get(flight[0]).add(Arrays.copyOfRange(flight, 1, flight.length));
        }

        int[] minHops = new int[n];
        Arrays.fill(minHops, -1);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[] {src, 0, 1});

        while (pq.size() > 0) {
            int[] current = pq.poll();
            int node = current[0];
            int time = current[1];
            int hop = current[2];

            if (hop - 2 > k) {
                continue;
            }

            if (node == dst) {
                return time;
            }

            if (minHops[node] > 0 && minHops[node] <= hop) {
                continue;
            }
            minHops[node] = hop;

            for(int[] toGo : flightMap.get(node)) {
                int newNode = toGo[0];
                int newTime = time + toGo[1];
                int newHop = hop + 1;

                pq.offer(new int[] {newNode, newTime, newHop});
            }
        }

        return -1;
    }
}