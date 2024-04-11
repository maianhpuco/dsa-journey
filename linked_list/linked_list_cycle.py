#Link : https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Time O(n^2)
        Space O(n)
        3 2 0 -4 2 0 -4 
        '''
        traveled = []
        while head:
            if head in traveled:
                return True
            else:
                traveled.append(head)
            head = head.next
        return False
