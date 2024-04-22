#Link : https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
class Solution:

    def minimumPerimeter(self, neededApples: int) -> int:
        '''
        L: length of the unit square (top right)
        #apple ON the PERIMETER: f(L) = 12*L^2
        #apple collected = 12*L^2 + 12(L-1)^2 +  12(L-2)^2 + ...+ 12L(L-L)^2  
        n = L 
         = 12 * n * (n+1) * (2n+1) * 1/6 = 2 n * (n+1) * (2n+1) * 1/6  
        #perimeter g(L) = 8*L

        given a number neededApples, find the smallest i so that f(i) >= neededApples 
        630 => 1.002.570.660 1.000.000.000 
        '''
        r = ceil(pow(neededApples, 1 / 3))
        l = 0
        i = 0
        while l <= r:
            mid = l + (r - l) // 2
            if (2 * mid * (mid + 1) * (2 * mid + 1)) < neededApples:
                l = mid + 1
            else:
                i = mid
                r = mid - 1
        return i * 8
