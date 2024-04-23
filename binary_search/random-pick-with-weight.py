#Link: https://leetcode.com/problems/random-pick-with-weight/


class Solution:
    '''
    w = [1, 3] 
    picking 0: 1 / (1 + 3) = 0.25 
    picking 0: 3 / (1 + 3) = 0.75
    '''

    def __init__(self, w: List[int]):
        # create probabitily list here
        # [1, 1, 2, 4, 5] 100 (7.6900, 7.6900, 13.3800, 30.76, 38.4500)
        # acc = (7.6900, 15.3800, 28.76, 61.52, 100)
        total = sum(w)
        self.acc = []
        curr = 0
        for v in w:
            curr += 100 * v / total
            self.acc.append(round(curr, 4))

    def pickIndex(self) -> int:
        '''
        sum from left to right, return the number less t
        '''
        seed = randint(0, 10000) / 100  #23,4589
        print(seed)
        return bisect_left(self.acc, seed)
