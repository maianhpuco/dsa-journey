import collections
from typing import *


# Link: https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        '''
        original = [17,13,11,2,3,5,7] 
        deck = [2,13,3,11,5,17,7] 
        2 [3,11,5,17,7,13]
        2 3 [5,17,7,13,11]
        2 3 5 [7,13,11,17]
        2 3 5 7 [11,17, 13]
        2 3 5 7 11 [13 17]
        2 3 5 7 11 13 17 -> [2,13,3,11,5,17,7] 
        ---
        [17]
        [13 ,17] - thêm 13, last = 17 
        [11, 17, 13] - move 17 to font, add 11 to font, last = 13 
        [7, 13, 11, 17] - move 13 to font, add 7 to font, last = 17 
        move last -> font add another number to font 
        '''
        deck.sort()  #[2,3,5,7,11, 13, 17]
        results = collections.deque()  # note: reverse order at the end
        while len(deck) > 0:
            if len(results) > 0:
                last = results.popleft()
                results.append(last)
            results.append(deck.pop())
        results.reverse()
        return results


if __name__ == "__main__":
    input = [17, 13, 11, 2, 3, 5, 7]
    sol = Solution()
    out = sol.deckRevealedIncreasing(input)
    print(out)
