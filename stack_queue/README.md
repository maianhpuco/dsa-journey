
# STACK: LIFO: last-in-first-out

- operation: push(), pop(), peek(), isEmpty(), isFull()
  + push(): move to the stack
  + pop(): take out, on the top 
  + peak(): just view (not taking out), on the top of Stack, O(1) 
  + push / pop : O(1)
  + size: kiểm tra số phần tử trong stack O(1)
    
- Stack implementation (cài đặt) 
  +  sử dụng dynamic array (có thể resize, trong python)
  +  sử dụng linked list
  +  Python: list, queue.LifoQueue, collections.deque 

- Stack cài bằng list thì có thể loop nhưng cài bằng linked list:
- Cách 1 (ko chính thống)
  ```python
  for i in range(stack.size()):
    # do sthing
    # this is wrong
  ```
- Cách 2 (chính thống)
  ```python
  while not stack.isEmpty():
    // do smthing 
  ```
# QUEUE 
- 
