from typing import List

class Queue:
    
    def __init__(self) -> None:
       self.items: List[object] = []
        
    def enqueue(self, item: object) -> None:
        self.items.append(item)
        
    def dequeue(self) -> object:
        return self.items.pop(0)
        
    def front(self) -> object:
        return self.items[0]
        
    def size(self) -> int:
        return len(self.items)