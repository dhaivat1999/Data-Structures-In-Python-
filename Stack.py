class Stack:
    def __init__(self):
        self.stack=[]
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        print("Popped Element: " + str(data))

    def peek(self):
        print(self.stack[-1])
    
    def size(self):
        print(len(self.stack))

    def display(self):
        for num in self.stack:
            print(num)
stack=Stack()
x=input("Enter the value to push in stack")
stack.push(x)
stack.push(12)
stack.display()
stack.pop()
# stack.display()