#Link: https://leetcode.com/problems/happy-number/


class Solution:

    def isHappy(self, n: int) -> bool:
        '''
        19 -> 82 -> 68 > 100
        2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 2 
        -> there are circular in the results 
        -> detecting the circular
        -> Brute force (or 2 pointers)
        '''
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.f(n)
            if n == 1:
                return True
        return False

    def f(self, x):
        '''
        189 = 9 and 8 and 1
        9 = 19%10
        8 = 18%10 
        1 = 1%10
        '''
        total = 0
        while x > 0:
            divided = x % 10
            total += divided * divided
            x //= 10
        return total
