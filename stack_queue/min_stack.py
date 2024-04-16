# Link: https://leetcode.com/problems/min-stack/


class MinStack:
    '''
    Idea: đưa 1 biến min vào trong init, sẽ thay đổi mỗi lần push
    '''

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_values.append(val)
        else:
            min_value = self.min_values[-1]
            if val < min_value:
                self.min_values.append(val)
            else:
                self.min_values.append(min_value)
        self.stack.append(val)

    def pop(self) -> None:
        self.min_values.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
