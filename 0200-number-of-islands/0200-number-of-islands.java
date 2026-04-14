import java.util.*;

class Solution {
    public int numIslands(char[][] grid) {
        int result = 0;

        ArrayDeque<int[]> stack = new ArrayDeque<>();

        for (int i = 0; i < grid.length; i++ ) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '0') {
                    continue;
                }

                result++;

                stack.push(new int[] {i, j});
                while (true) {
                    int[] current = stack.pop();

                    if (current == null) {
                        break;
                    }

                    int _i = current[0];
                    int _j = current[1];

                    if (_i < 0 || _i >= grid.length || _j < 0 || _j >= grid[0].length) {
                        break;
                    }

                    if (grid[_i][_j] == '0') {
                        break;
                    }

                    grid[_i][_j] = '0';

                    stack.push(new int[] {_i - 1, _j});
                    stack.push(new int[] {_i, _j - 1});
                    stack.push(new int[] {_i + 1, _j});
                    stack.push(new int[] {_i, _j + 1});
                }
            }
        }

        return result;
    }
}