from collections import deque

x = 3

stack = [] 
stack.append(x)
stack.pop()

queue = deque()
queue.append(x)
queue.popleft()