from collections import *

class MyStack:

    def __init__(self):
        self.qData = deque()
        self.qTemp = deque()
        

    def push(self, x: int) -> None:
        self.qData.append(x)
        

    def pop(self) -> int:
        while len(self.qData) > 1:
            self.qTemp.append(self.qData.popleft())
        result = self.qData.popleft()
        while len(self.qTemp) > 0:
            self.qData.append(self.qTemp.popleft())

        return result
    
        
    def top(self) -> int:
        while len(self.qData) > 1:
            self.qTemp.append(self.qData.popleft())
        result = self.qData.popleft()
        self.qTemp.append(result)
        while len(self.qTemp) > 0:
            self.qData.append(self.qTemp.popleft())

        return result
        

    def empty(self) -> bool:
        
        return len(self.qData) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()