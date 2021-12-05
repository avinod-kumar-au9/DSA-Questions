class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, x):
        self.__stack.append(x)
    def pop(self):
        return self.__stack.pop()
    def peek(self):
        return self.__stack[- 1]
    def is_empty(self):
        return len(self.__stack) == 0
def solve(array):
    s = Stack()
    idx = 0
    count = 0
    while idx < len(array):
        elem = array[idx]
        if s.is_empty():
            s.push(elem)
        
        else:
            while not s.is_empty() and s.peek() < elem :
                print(s.peek(), elem)
                s.pop()
            s.push(elem)
        idx += 1
        print(s)
    #circularly
    while not s.is_empty():
        if count < len(array):
            if idx >= len(array):
                idx = idx - len(array) 
            elem = array[idx]
            while s.peek() < elem:
                print(s.peek(), elem)
                s.pop()
            idx+=1
            count+=1
        else:
            while not s.is_empty():
                print(s.peek(), -1)
                s.pop()
                
if __name__ == '__main__':
    solve([1, 5, 2, 3, 7, 2])