from typing import List


class Stack[T]:
    def __init__(self):
        self.stack: List[T] = []
    
    def push(self, item: T):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()