class Queue2stack():
    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def enqueue(self,element):
        self.instack.append(element)

    def dequeue(self,element):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

        

q=Queue2stack()

q.enqueue(3)

print(q.instack)