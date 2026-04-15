class Solution {
    public void rotate(int[][] matrix) {
        for (int i = 0; i < matrix.length / 2; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                swap(matrix, i, j, matrix.length - 1 - i, j);
            }
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0 + i; j < matrix[0].length; j++) {
                swap(matrix, i, j, j, i);
            }
        }
    }

    void swap(int[][] matrix, int i, int j, int p, int q) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[p][q];
        matrix[p][q] = temp;
    }
}