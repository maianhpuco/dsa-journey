# link: https://leetcode.com/problems/pascals-triangle/


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        @lru_cache
        def f(i, j):
            '''
            choosing value for postion (i, j) 
            '''
            if j == 0 or i == j:
                return 1
            return f(i - 1, j - 1) + f(i - 1, j)

        ans = [[0 for _ in range(i + 1)] for i in range(numRows)]
        for row in range(numRows):
            for col in range(row + 1):
                ans[row][col] = f(row, col)
        return ans
