# https://leetcode.com/problems/merge-two-sorted-lists/

# Solution: tạo 1 linked-list mới là tmp


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - list1 - x: i: 1 -> n  
        - list2 - y: j: 1-> m 
        if x(i) > y(j): 
            
            j+=1 
        # If value at y(i) is equal or smaller, 
            connect x(i).next = y(j)
            j += 1 
        else i += 1  
        # if i == n: j+=1
        # if j == m: i+=1  
        Example:
        list 1: 3 > 4 > 7
                ^      
        list 2: 1 > 2 > 5 
                ^
                1> 3> 4 >7 | 3 
                    
                2 5 

        '''
        dummy = tmp = ListNode(1)
        while list1 and list2:
            if list2.val <= list1.val:
                tmp.next = list2
                list2 = list2.next
            else:
                tmp.next = list1
                list1 = list1.next
            tmp = tmp.next

        tmp.next = list1 or list2
        return dummy.next
