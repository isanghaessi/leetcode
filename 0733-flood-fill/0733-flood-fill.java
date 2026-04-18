class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) {
            return image;
        }

        fill(image, sr, sc, color, image[sr][sc]);

        return image;
    }

    void fill(int[][] image, int i, int j, int color, int originColor) {
        if (i < 0 || i >= image.length || j < 0 || j >= image[0].length) {
            return;
        }

        if (image[i][j] != originColor) {
            return;
        }

        image[i][j] = color;

        fill(image, i - 1, j, color, originColor);
        fill(image, i + 1, j, color, originColor);
        fill(image, i, j - 1, color, originColor);
        fill(image, i, j + 1, color, originColor);
    }
}