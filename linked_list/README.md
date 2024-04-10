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
---- 

