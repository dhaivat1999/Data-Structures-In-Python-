class Queue:
    def __init__(self):
        self.queue=[]
    
    def isEmpty(self):
        return self.queue == []

    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        data=self.queue[0]
        del self.queue[0]
        print("Dequeued element: " + str(data))

    def peek(self):
        print(self.queue[0])

    def sizequeue(self):
        print(len(self.queue))

queue= Queue()
x= input("Enter the value")
queue.enqueue(x)
queue.peek()
queue.enqueue(5)
queue.enqueue(19)
queue.sizequeue()