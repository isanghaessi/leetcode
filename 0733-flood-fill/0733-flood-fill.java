class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        fill(image, sr, sc, color, image[sr][sc], new HashSet<>());

        return image;
    }

    void fill(int[][] image, int i, int j, int color, int originColor, Set<String> path) {
        if (i < 0 || i >= image.length || j < 0 || j >= image[0].length) {
            return;
        }

        String currentPath = "" + i + j;
        if (path.contains(currentPath)) {
            return;
        }
        path.add(currentPath);

        if (image[i][j] != originColor) {
            return;
        }

        image[i][j] = color;

        fill(image, i - 1, j, color, originColor, path);
        fill(image, i + 1, j, color, originColor, path);
        fill(image, i, j - 1, color, originColor, path);
        fill(image, i, j + 1, color, originColor, path);
    }
}