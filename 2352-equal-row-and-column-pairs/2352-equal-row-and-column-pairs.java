class Solution {
    public int equalPairs(int[][] grid) {
        Map<String, Integer> rowCounter = new HashMap<>();

        for (int i = 0; i < grid.length; i++) {
            StringBuilder sb = new StringBuilder();

            for (int j = 0; j < grid[0].length; j++) {
                sb.append(String.valueOf(grid[i][j]));
                sb.append(",");
            }

            String key = sb.toString();
            int value = rowCounter.getOrDefault(key, 0) + 1;
            rowCounter.put(key, value);
        }

        int result = 0;

        for (int i = 0; i < grid.length; i++) {
            StringBuilder sb = new StringBuilder();

            for (int j = 0; j < grid[0].length; j++) {
                sb.append(String.valueOf(grid[j][i]));
                sb.append(",");
            }

            String key = sb.toString();
            
            if (rowCounter.containsKey(key)) {
                result += rowCounter.get(key);
            }
        }

        return result;
    }
}