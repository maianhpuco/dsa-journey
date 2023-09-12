# https://leetcode.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head):
        if not head:
            return head
        _list = []
        while head:
            _list.append(head)
            head = head.next
        print([node.val for node in _list])
        self.rev(_list)
        print([node.val for node in _list])

        dummy = other_head = ListNode(1)
        for curr in _list:
            other_head.next = curr
            other_head = other_head.next
        other_head.next = None
        return dummy.next

    def rev(self, array_input):
        """
        This is the function to reverse and array, needed to remember!
        REMEMBER: LIST IS MUTABLE
        """
        l, r = 0, len(array_input) - 1
        while l < r:
            array_input[l], array_input[r] = array_input[r], array_input[l]
            l, r = l + 1, r - 1

    # def reverseLinkedList_ver2(self, head):


def reverse_a_list(array_input):
    """
    This is the function to reverse and array, needed to remember!
    REMEMBER: LIST IS MUTABLE
    """

    l, r = 0, len(array_input) - 1
    while l < r:
        array_input[l], array_input[r] = array_input[r], array_input[l]
        l, r = l + 1, r - 1


if __name__ == "__main__":
    A = [1, 2, 3]
    reverse_a_list(A)
    print("here is A again", A)
    "reverse a node but using the linked list, input will only be a Node (named head)"
    input = [1, 2, 3, 4]
    head = ListNode(input[0])
    curr = head
    for n in input[1:]:
        curr.next = ListNode(n)
        curr = curr.next

    s = Solution().reverseLinkedList(head)
