![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/e032cd32-8494-43b1-ae65-0b8ddd0787ba)# Singly Linked List

- Go from left to right
- Time complexity to remove node #k is O(k)
- Operation with linked list:
  - Deletion
  ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/f9bfd29b-1800-4f15-b323-664e4b7a3b0a)

  - Insertion
  ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/03df7053-ebbe-4341-95f8-90b9b44a929c)


```python
class Node
    def __init__(self, val=0, next_node=None):
        self.val=val
        self.next_node = next_node
```

# Double linked list 
- 2-way traversal
- Time complexity to update/ insert/ delete = O(k)
- Application: **LRU cache** (list recently used cached) 
```python
class Node:
  def __init__(self, val=0, next_node=None, prev_node=None):
    self.val = val
    self.next_node = next_node
    self.prev_node = prev_node 
```
 ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/3e33513e-8bba-468e-a761-a4547169e6c7)

[?] LRUcache là gì ? một chiến lược cache, dùng dsach liên kết đôi mem-catch 

**Example**: 
1. https://leetcode.com/problems/reverse-linked-list/
2. https://leetcode.com/problems/merge-two-sorted-lists/description/
3. https://leetcode.com/problems/linked-list-cycle/
4. https://leetcode.com/problems/happy-number/description/ 



---------
**Important Note**
In Python, when you assign one variable to another, as in curr = head, you are not creating a new object; rather, you are creating a new reference to the same object in memory. Therefore, modifying curr or head will affect the same underlying object.


```python 
------ 
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating a linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

head = node1
curr = head

# Modifying curr
curr.val = 10
print("After modifying curr:")
print("curr:", curr.val)
print("head:", head.val)

# Modifying head
head.val = 20
print("After modifying head:")
print("curr:", curr.val)
print("head:", head.val)

ver2_node1 = ListNode(5)
ver2_node2 = ListNode(6)

ver2_node1.next = ver2_node2

head.next = ver2_node1
print("After modifying head.next by assigning to new memory place:")
print("curr:", curr.next.val)
print("head:", head.next.val)

#Only this does n't change
head = head.next
print("After modifying head.next by assigning to new memory place:")
print("curr:", curr.val)
print("head:", head.next.val)
 ```

Result
```python
After modifying curr:
curr: 10
head: 10
After modifying head:
curr: 20
head: 20
After modifying head.next by assigning to new memory place:
curr: 5
head: 5
After modifying head.next by assigning to new memory place:
curr: 20
head: 5 
```

Example for the 1. Reverse linked list problem 

pay attention to the part

```python
  #Wrong answer if:  ######################## 
        #while head:  # last head = 5
        #    prev = curr  # temporarily save the curr
        #    curr = head  #cut the current head
        #    curr.next = prev  # reverse  # lúc này curr thay đổi thì head cũng thay đổi luôn

        #    print("1. curr", curr.val, "head", head.val, head.next)
        #    head = head.next
        #    if head:
        #        print("1. curr", curr.val, "head", head.val)
        #return curr
        ######################################  
```

```python 
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

        #Wrong answer if:  ######################## 
        #while head:  # last head = 5
        #    prev = curr  # temporarily save the curr
        #    curr = head  #cut the current head
        #    curr.next = prev  # reverse  # lúc này curr thay đổi thì head cũng thay đổi luôn

        #    print("1. curr", curr.val, "head", head.val, head.next)
        #    head = head.next
        #    if head:
        #        print("1. curr", curr.val, "head", head.val)
        #return curr
        ###################################### 

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
 ```

2. Dùng Dummy để dễ xóa node:
   ![image](https://github.com/maianhpuco/dsa-journey/assets/34562568/b226e032-bfa5-4377-9585-be85ac7a911d)





