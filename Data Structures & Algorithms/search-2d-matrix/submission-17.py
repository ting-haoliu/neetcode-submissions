class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search
        # T: O(log(m * n))
        # S: O(1)
        m = len(matrix)
        n = len(matrix[0])
        L, R = 0, m * n - 1

        while L <= R:
            mid = (L + R) // 2
            r, c = mid // n, mid % n

            if matrix[r][c] < target:
                L = mid + 1
            elif matrix[r][c] > target:
                R = mid - 1
            else:
                return True

        return False
        