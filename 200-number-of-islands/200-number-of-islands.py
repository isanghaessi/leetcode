class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j:
                
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
                
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    answer += 1
                    dfs(i, j)
        
        return answer