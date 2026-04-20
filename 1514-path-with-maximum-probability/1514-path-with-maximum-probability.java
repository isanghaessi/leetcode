class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        Map<Integer, List<int[]>> edgeMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            edgeMap.put(i, new ArrayList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            edgeMap.get(edges[i][0]).add(new int[] {edges[i][1], i});
            edgeMap.get(edges[i][1]).add(new int[] {edges[i][0], i});
        }

        double[] maxProbs = new double[n];
        Arrays.fill(maxProbs, 0);

        PriorityQueue<List<Number>> pq = new PriorityQueue<>((a, b) -> Double.compare((double)b.get(1), (double)a.get(1)));
        List<Number> item = new ArrayList<>();
        item.add(start_node);
        item.add((double)1);
        pq.offer(item);

        while (pq.size() > 0) {
            List<Number> current = pq.poll();
            int node = (int)current.get(0);
            double possibility = (double)current.get(1);

            if (node == end_node) {
                return possibility;
            }

            if (maxProbs[node] > possibility) {
                continue;
            }

            maxProbs[node] = possibility;

            List<int[]> toGos = edgeMap.get(node);
            for (int[] toGo: toGos) {
                int newNode = toGo[0];
                double newPossibility = possibility * succProb[toGo[1]];
                List<Number> newItem = new ArrayList<>();
                newItem.add(newNode);
                newItem.add(newPossibility);
                pq.offer(newItem);
            }

            toGos.clear();
        }

        return 0;
    }
}