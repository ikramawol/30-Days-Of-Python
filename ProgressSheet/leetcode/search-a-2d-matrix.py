class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n*m - 1


        def _matrix(mid):
            row = mid // m
            col = mid % m
            return [row, col]

        
        while left <= right:
            mid = (left + right)//2

            val = _matrix(mid)
            if matrix[val[0]][val[1]] == target:
                return True
            if matrix[val[0]][val[1]] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):

        #         if matrix[i][j] == target:
        #             return True
        # else:
        #     return False