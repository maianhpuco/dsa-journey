# PROBLEM: 1. https://leetcode.com/problems/reverse-linked-list/
# DESCRIPTION
'''
providing 2 solution
- reverse_ver1: brute force: Time and Space O(n) 
- reverse_ver2: try to loop and reverse .next of each element of the linked list Time O(n) Space O(1) 
'''
from typing import *


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.reverse_ver1(head)
        return self.reverse_ver2(head)

    def reverse_ver1(self, head: ListNode) -> ListNode:
        '''
        Brute Force (18%)
        Time: O(n); Space: O(n)
        '''
        #check empty head
        if not head:
            return head
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        node_list = self.rev(
            node_list)  # hoặc dùng build-in node_list.reverse()
        # node_list: ard construct a list node, can we return node_list ? there are no "door-in", and "door-out"
        # list-node: the boat [5,4,3,2,1]; but there is no way to access using .next
        dummy = tmp = ListNode(1)
        #[1]
        #[1, 5, 4, 3, 2, 1,] -> give 1.next (5); 1: anchor and [5,4,3,2,1]: the boat
        for node in node_list:
            tmp.next = node
            tmp = tmp.next
        tmp.next = None
        return dummy.next

    @staticmethod
    def rev(arr):
        l, r = 0, len(arr) - 1
        while l < r:
            #swap using tuple
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1
        return arr

    def reverse_ver2(self, head: ListNode) -> ListNode:
        '''
        Idea: Travel from left -> right, 
        1>2>3>4>5>Null
        Null<1<2 3>4>5 
        ...
        n = 1 
        Current: 
        - 1.next = 2; want 1.next = None 
        - 2.next = 3; want 2.next = 1 
        Null<1<2<3<4<5<anchor
          ^curr 
             ^head 

             ^
            prev = 1.next (store)
            1.next = None
            
       --- 
       None < 1 
       prev = [1>]2>3>4 ... 
       Want: 
        head = 1 
        head.next = None 
        head = prev.next (2)
        curr = 1 
       --- 
       curr = None 
        while head: 2 
            prev = head (we need .next: head.next = 2 > 3 .. )
            head.next = curr (1 > None)
            curr = prev.next (2 > 1 > None)
            prev.next (continue travel the loop 2>3)
        '''
        if not head:
            return head
        '''
        - prev: traveled value (of curr)
        - curr: new linked list (cut each element of the head and put into its list)
        - head: current linked list 
        '''
        curr = None
        while head:  # last head = 5
            prev = curr  # temporarily save the curr
            curr = head  #cut the current head
            print("1. curr", curr.val, "head", head.val)
            head = head.next
            if head:
                print("2. curr", curr.val, "head", head.val)
                print("--")
            curr.next = prev  # reverse

        #Wrong anwer if
        #while head:  # last head = 5
        #    prev = curr  # temporarily save the curr
        #    curr = head  #cut the current head
        #    curr.next = prev  # reverse  # lúc này curr thay đổi thì head cũng thay đổi luôn

        #    print("1. curr", curr.val, "head", head.val, head.next)
        #    head = head.next
        #    if head:
        #        print("1. curr", curr.val, "head", head.val)
        #return curr


if __name__ == "__main__":
    # Create a linked list
    nodes = [ListNode(val) for val in [1, 2, 3, 4, 5]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    sol = Solution()
    output = sol.reverse_ver2(nodes[0])
    while output:
        print(output.val, end=" ")
        output = output.next
