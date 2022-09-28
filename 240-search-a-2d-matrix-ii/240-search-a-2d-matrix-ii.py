class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        while 0 <= i and i < len(matrix) and 0 <= j and j < len(matrix[0]):
            print(i, j, matrix[i][j])
            if matrix[i][j] == target:
                
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        
        return False