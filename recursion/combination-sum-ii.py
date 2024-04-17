# Link: https://leetcode.com/problems/combination-sum-ii/

# FIRST TRY: TIME LIMITED EXCEED


class Solution_1:  # time exceed

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        '''
        Idea: candidates = [10,1,2,7,6,1,5]
                    i = 1.     ^1 
                    i = 2.       ^2  
                    i = 3.              ^5
                    i = 4.                ^6
        B1: dien dat bang loi lai quy trinh back track 
        curr_pointer
        [0]
        [1, 2, 6]
        [?] update pointer ? [1,2,1,_] 1,2,1 ko work, pointer đang ở 5-> 
                curr_s = [1,2,1] -> [1, 2] 
                (1 ko work -> pop 1 ra, bt [1,2], nhưng search tiep o vi tri tiep theo cua i=3)
                curr_p = [1,2,5] 
            -> backtrack lai [1,2]     -> search tiep tu [5] -> khong work , pointer = [1,2,6] 
            -> backtrack lai [1]       -> search tiep tu [7] -> work -> added vao
        [?] neu search het cac vi tri ma ko tim dc => update pointer  
        '''
        ans = []
        current_solution = []
        pointers = [-1]

        def choose(i):  #pointers = [-1] loop from 0
            """
                Choose the i-th position of th e result list 
            """
            #base-case
            if sum(current_solution) == target:
                res = current_solution.copy()
                res.sort()
                if res not in ans:
                    ans.append(res)
                return
            for idx, c in enumerate(candidates[pointers[-1] +
                                               1:]):  #[10,1,2,7,6,1,5]
                if c + sum(
                        current_solution
                ) <= target:  #[1,8,9,10] # smaller -> continue to search
                    current_solution.append(c)  #pointer = 3 (last) [1, 4]
                    pointers.append(pointers[-1] + idx + 1)
                    choose(i + 1)
                    current_solution.pop()
                    pointers.pop()
            #end of loop: neu tim het day ma van ko add dc so nao? [1, 8, 9, 10] -> backtrack lai
            if sum(current_solution) > target:
                pointers[-1] = pointers[-1] + 1  #pointers = [1]
                return

        choose(0)
        return ans


class Solution_2:

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        '''
        - Normal Backtracking: 
        current_solution: selected number 
        each candidate: 2 choice: add / not added, 1 <= candidates.length <= 100
            -> each position: 2^100
            -> all: 2^100 * 100  
        - New solution:
        current_solution: #time selected of that number 
        each candidate have k+1 choice (k: frequency in the candidates), vd k = 3 
        -> 3 choice: 
            -> each position: max k^50
            -> all: k^50 * 50        

        unique = [1, 2, 5], target = 5 
        freq   = [1, 3, 1]
        [1, 2, 2]
        cs     = [1, 2] sum = 5 -> return 
        cs.    = [1, 1] sum = 3 -> move i+1 
        cs     = [1, 0] sum = 1 -> move i+1 
        '''
        unique_candidates = list(set(candidates))
        freq = [0 for _ in unique_candidates]
        for idx, u in enumerate(unique_candidates):  #O(n^2)
            for c in candidates:
                if u == c:
                    freq[idx] += 1  # co the doi thanh dictionary
        ans = []
        current_solution = []

        def choose(i):
            '''
                choosing the i-th position for the current_solution;
                each i will have k+1 choice; k = freq[i]  = 2 -> 0, 1, 2 
            '''
            # base-case
            s = self.compute_sum(current_solution, unique_candidates)
            if s > target:
                return
            if i == len(unique_candidates):
                if s == target:
                    res = self.translate(current_solution, unique_candidates)
                    ans.append(res.copy())
                return
            for c in range(freq[i] + 1):
                current_solution.append(c)
                choose(
                    i +
                    1)  # backtracking cho nay ntn [2, 1, 0, 0 , 0] --> return
                current_solution.pop()

        choose(0)
        return ans

    @staticmethod
    def compute_sum(curr_sol, unique_can):
        s = 0
        for f, c in zip(curr_sol, unique_can):
            s += c * f
        return s

    @staticmethod
    def translate(curr_sol, unique_can):
        res = []
        for f, c in zip(curr_sol, unique_can):
            if f > 0:
                for i in range(f):
                    res.append(c)
        return res
