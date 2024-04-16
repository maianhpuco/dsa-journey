#LINK: https://leetcode.com/problems/number-of-recent-calls/
class RecentCounter:
    MAX_SPAN = 3000
    '''
    [1] [-2999, 1] 1 
    [1, 100] [-2900, 100] 3 
    st = [1, 100, 3001] [1, 3001] 3 
    i: 0-len(st)
        if st[i] >= 1 and st[i] <= 3001 
    [?] Tại sao phải dùng Queue ở đây: 
    Queue chỉ lưu lại phần tử trong khoảng 3000, còn lại bỏ đi
    Mỗi lần ping mình sẻ check dequeue

    -> giảm Space complexity 
    Phân tích time and space complexity ntn ? 
    '''

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t - self.MAX_SPAN:
            self.queue.popleft()
        return len(self.queue)reverse = True


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
