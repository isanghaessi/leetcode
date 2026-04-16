class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        int iMin = 0;
        int iMax = matrix.length - 1;
        int jMin = 0;
        int jMax = matrix[0].length - 1;
        
        int i = iMin;
        int j = jMin;
        addAndMark(matrix, i, j, result);
        while (iMin <= iMax && jMin <= jMax) {
            while (j + 1 <= jMax) {
                j++;
                addAndMark(matrix, i, j, result);
            }
            iMin++;

            while (i + 1 <= iMax) {
                i++;
                addAndMark(matrix, i, j, result);
            }
            jMax--;

            while (j - 1 >= jMin) {
                j--;
                addAndMark(matrix, i, j, result);
            }
            iMax--;

            while (i - 1 >= iMin) {
                i--;
                addAndMark(matrix, i, j, result);
            }
            jMin++;
        }

        return result;
    }

    void addAndMark(int[][] matrix, int i, int j, List<Integer> result) {
        if (matrix[i][j] > 100) {
            return;
        }

        result.add(matrix[i][j]);
        matrix[i][j] = 101;
    }
}