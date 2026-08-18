class Solution {
    public int equalPairs(int[][] grid) {
        Map<List<Integer>, Integer> rowCounter = new HashMap<>();

        for (int i = 0; i < grid.length; i++) {
            List<Integer> ls = new ArrayList<>();

            for (int j = 0; j < grid[0].length; j++) {
                ls.add(grid[i][j]);
            }

            int value = rowCounter.getOrDefault(ls, 0) + 1;
            rowCounter.put(ls, value);
        }

        int result = 0;

        for (int i = 0; i < grid.length; i++) {
            List<Integer> ls = new ArrayList<>();

            for (int j = 0; j < grid[0].length; j++) {
                ls.add(grid[j][i]);
            }

            if (rowCounter.containsKey(ls)) {
                result += rowCounter.get(ls);
            }
        }

        return result;
    }
}