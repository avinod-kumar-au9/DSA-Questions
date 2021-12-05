class MinStack:

    def __init__(self):
        self.s = []
        self.a = []

    def push(self, x: int) -> None:
        if self.a == [] or self.a[-1] >= x:
            self.a.append(x)
        self.s.append(x)

    def pop(self) -> None:
        y=self.s.pop()
        if y == self.a[-1]:
            self.a.pop()

    def top(self) -> int:
        if len(self.s) == 0:
            return None
        else:
            return(self.s[-1])

    def getMin(self) -> int:
        if len(self.a)==0:
            return None
        else:
            return self.a[-1]

    
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())