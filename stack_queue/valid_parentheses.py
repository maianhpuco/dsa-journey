#Link https://leetcode.com/problems/valid-parentheses/
MAP_PAIR = {"[": "]", "{": "}", "(": ")"}


class Solution:

    def isValid(self, s: str) -> bool:
        '''
        Dung stack
        - traversal from right -> left and adding to a stack S 
        - checking if a pair a found -> remove 
        -> if there is no element in S -> valid
        '''

        stack = []
        for index, i in enumerate(s):
            #if left character
            if i in MAP_PAIR:
                stack.append(i)
            else:
                #if right character
                if not stack:
                    return False
                if MAP_PAIR.get(stack.pop()) != i:
                    #note: not using stack[-1] vì tránh th stack empty
                    return False
        return len(stack) == 0
