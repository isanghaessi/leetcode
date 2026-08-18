class Solution {
    public int equalPairs(int[][] grid) {
        Map<String, Integer> rowCounter = new HashMap<>();
        Map<String, Integer> colCounter = new HashMap<>();

        for (int i = 0; i < grid.length; i++) {
            StringBuilder rowSb = new StringBuilder();
            StringBuilder colSb = new StringBuilder();

            for (int j = 0; j < grid[0].length; j++) {
                rowSb.append(String.valueOf(grid[i][j]));
                rowSb.append(",");

                colSb.append(String.valueOf(grid[j][i]));
                colSb.append(",");
            }

            String rowKey = rowSb.toString();
            int rowValue = rowCounter.getOrDefault(rowKey, 0) + 1;
            rowCounter.put(rowKey, rowValue);

            String colKey = colSb.toString();
            int colValue = colCounter.getOrDefault(colKey, 0) + 1;
            colCounter.put(colKey, colValue);
        }
        
        int result = 0;

        for (String rowKey : rowCounter.keySet()) {
            for (String colKey : colCounter.keySet()) {
                if (rowKey.equals(colKey)) {
                    result += rowCounter.get(rowKey) * colCounter.get(colKey);
                }
            }
        }

        return result;
    }
}