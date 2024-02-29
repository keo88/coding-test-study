from heapq import heappush, heappop

class MinStack:

    def __init__(self):
        self.minNumber = None
        self.stack = []
        self.hq = []
        self.popped = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        heappush(self.hq, val)
        

    def pop(self) -> None:
        if len(self.stack) > 0:
            item = self.stack.pop()
            if item in self.popped:
                self.popped[item] += 1
            else:
                self.popped[item] = 1

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if len(self.hq) == 0:
            return None
        while self.hq[0] in self.popped:
            item = heappop(self.hq)
            if self.popped[item] <= 1:
                del self.popped[item]
            else:
                self.popped[item] -= 1
        if len(self.hq) > 0:
            return self.hq[0]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
