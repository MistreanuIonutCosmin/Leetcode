class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if len(self.min_stack) == 0 or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        
        self.data.append(x)
        
    def pop(self) -> None:
        if self.data[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.data.pop()
            
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
