class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        right = max(matrix)
        left = min(matrix)

        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == target:
                    return True
        else:
            return False