from typing import List, TypeVar


T = TypeVar('T')


class Stack[T]:
    def __init__(self):
        self._stack: List[T] = []
    
    def push(self, item: T):
        self._stack.append(item)
    
    def pop(self):
        return self._stack.pop()
    
    def empty(self):
        return len(self._stack) == 0