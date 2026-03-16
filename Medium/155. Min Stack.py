
class MinStack:
    def __init__(self):
        self.arr = []
        self.mins = []
    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.mins:
           self.mins.append(min(val, self.mins[-1])) 
        else:
            self.mins.append(val)
    def pop(self) -> None:
        self.arr.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Stack + Shadow Stack with running minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()