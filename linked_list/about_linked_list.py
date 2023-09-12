"""
NOTE: 
- USING THE "dummy" variable as the key keeper for the linked list 
- a = b = ListNode(1) # node reference; a and b are pointing to the same node 1 

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# REVERSE THE LINKED LIST


class Solution:
    def reverse_linkedlist(self, head: ListNode):
        if not head:
            return head
        _list = []
        while head:
            _list.append(head)
            head = head.next
        _list.reverse()

        dummy, otherhead = ListNode(1)
        for curr in _list:
            otherhead.next = curr
            # move otherhead
            otherhead = otherhead.next
        otherhead.next = None

        return dummy.next


if __name__ == "__main__":
    a = b = ListNode(1)  # start
    c = ListNode(3)
    d = ListNode(4)

    a.next = c  # b.next = c => u = b.next then u.val = 3

    a = a.next
    print("a", a.val)  # a = 3
    a.next = d
    a = a.next
    print("a", a.val)
    u = b.next
    print("b next ", u.val)
