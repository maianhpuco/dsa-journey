#Link ; https://leetcode.com/problems/arranging-coins/submissions/1239904592/


class Solution:

    def arrangeCoins(self, n: int) -> int:
        '''
        f(i) = num_row
        [1, 2, 3, 4, 5, 6] 
        [1, 3, ^6, 10, 15, 21] #vị trí 2 
        vd n = 5 -> bisect_left
        '''

        left = 1
        right = n

        def calcCoinNeeded(rows):
            return rows * (1 + rows) // 2  #cap so cong

        ans = 1
        while left <= right:
            mid = left + (right - left) // 2
            if calcCoinNeeded(mid) <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
