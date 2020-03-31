class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
    def insertStart(self,data):
        self.size+=1
        newNode=Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode=self.head
            self.head =newNode

    def insertEnd(self,data):
        self.size+=1
        newNode= Node(data)
        actualNode=self.head
        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode

        actualNode.nextNode=newNode

    def remove(self,data):
        if self.head is None:
            return
        self.size-=1
        currentNode= self.head
        previousNode= None

        while currentNode.data != data:
            previousNode=currentNode
            currentNode=currentNode.nextNode

        if previousNode is None:
            self.head=currentNode.nextNode
        else:
            previousNode.nextNode=currentNode.nextNode

    def traverseList(self):
        actualNode=self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode=actualNode.nextNode
    


ll=LinkedList()

ll.insertStart(12)
ll.insertStart(10)
ll.insertStart(11)
ll.insertStart(15)
ll.insertStart(17)
ll.insertStart(15)
ll.insertEnd(1)
ll.insertEnd(145)
ll.insertEnd(566)
ll.remove(10)

ll.traverseList()