class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        int iMin = 0;
        int iMax = matrix.length - 1;
        int jMin = 0;
        int jMax = matrix[0].length - 1;
        
        while (iMin <= iMax && jMin <= jMax) {
            for (int j = jMin; j <= jMax; j++) {
                result.add(matrix[iMin][j]);
            }
            iMin++;

            for (int i = iMin; i <= iMax; i++) {
                result.add(matrix[i][jMax]);
            }
            jMax--;

            if (iMin <= iMax) {
                for (int j = jMax; j >= jMin; j--) {
                    result.add(matrix[iMax][j]);
                }
            }
            iMax--;

            if (jMin <= jMax) {
                for (int i = iMax; i >= iMin; i--) {
                    result.add(matrix[i][jMin]);
                }
            }
            jMin++;
        }

        return result;
    }
}