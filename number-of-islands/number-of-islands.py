class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:       
        def find_island(i, j, is_first):
            nonlocal answer
            
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] == '0':
                return
            else:
                if is_first:
                    answer += 1
                grid[i][j] = '0'
                to_go = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
                for tg in to_go:
                    find_island(*tg, False)
                
        answer = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                find_island(i, j, True)
        
        return answer
                