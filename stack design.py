class stack:
    def __init__(self):
        self.stack=[]

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        print("pop",self.stack.pop())
    
    def peek(self):
        print("peek",self.stack[-1])

    def stack_isempty(self):
        print("len",len(self.stack)==0)

if __name__ == "__main__":
    s=stack()

    s.push(2)
    s.push(4)
    s.push(6)
    s.push(8)
    s.pop()
    s.peek()
    s.pop()
    s.pop()
    
    s.stack_isempty()
    

    