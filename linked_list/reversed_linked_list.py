# https://leetcode.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    SPACE: O(N)
    TIME: O(3N) = O(N)

    [?] how to reduce the SPACE?
    SOLUTION 2: O(1)


    Head   [1>  2>^  3>  4> NULL]
    Curr    <1
    Prev N  <1

    prev = None
    --
    curr = head
    head = head.next
    curr.next = prev
    prev = curr


    pre
    function:
    - save prev before moving prev = curr
    - curr.next = prev
    - next = head.next
    - curr
    - move to next: curr = head.next

    """

    def reverseLinkedList_ver2(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseLinkedList_dead(self, head):
        """
        O(1) space solution
        """
        if not head:
            print("head is none")
            return head

        prev = None
        while head:
            curr = head
            curr.next = prev  # DEAD AT HERE head was pointing to the NONE value
            prev = curr
            head = head.next
            print("head, curr, prev", head, curr, prev)

        return prev

    def reverseLinkedList(self, head):
        if not head:
            return head
        _list = []
        while head:  # O(N)
            _list.append(head)
            head = head.next
        self.rev(_list)  # +O(N)

        dummy = other_head = ListNode(1)
        for curr in _list:  # O(N)
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
    head = ListNode(A[0])
    head.next = ListNode(A[1])
    curr = head
    print("before", head.next.val)
    curr = ListNode(A[2])
    print("after", head.next.val)

    reverse_a_list(A)
    print("here is A again", A)
    "reverse a node but using the linked list, input will only be a Node (named head)"
    input = [1, 2, 3, 4]

    #    head = ListNode(input[0])
    #    curr = head
    #    for n in input[1:]:
    #        curr.next = ListNode(n)
    #        curr = curr.next
    #
    #    s = Solution().reverseLinkedList(head)
    #    while s:
    #        print(s.val)
    #        s = s.next

    print("method 2")

    print("-------")
    input = [1, 2, 3, 4]
    head = ListNode(input[0])

    curr = head
    for n in input[1:]:
        curr.next = ListNode(n)
        curr = curr.next

    print("head.next", head.next.val)
    r = Solution().reverseLinkedList_ver2(head)
    while r:
        print(r.val)
        r = r.next
