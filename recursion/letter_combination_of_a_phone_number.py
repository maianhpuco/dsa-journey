#Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number


class Solution:
    MAPS = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        '''
        - INPUT: list of digit 
        digits = "23"
        - OUTPUT: all posible word combinations 
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        Mỗi vị trí max 4 lựa chọn
        tại mỗi vị trí, cần cân nhắc tiếp các vị trí cho các chỗ đứng sau = slg digit 
        time: gọi len(digits) = l: choosing tốn 4^l và l do join mảng các phần tử vs nhau
        - = > TC = 4^n * n
        space: 0(n) cho current_solution used từng lần vào choose(i)
        '''
        current_solution = []  # vd [a]
        ans = []

        def choose(i) -> None:
            '''
                choose i-th element for current solution
            '''
            #base
            if i == len(digits):
                ans.append("".join(current_solution.copy()))  #O(n)
                return
            for c in self.MAPS[digits[i]]:
                current_solution.append(c)  # hàm trc đệ quy
                choose(i + 1)
                current_solution.pop()  # hàm sau đệ quy

        if len(digits) == 0:
            return []
        choose(0)
        return ans
