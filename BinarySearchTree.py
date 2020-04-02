class Node(object):
    def __init__(self,data):
        self.data=data
        self.leftNode=None
        self.rightNode=None

class BST(object):
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data,self.root)

 #complexity of O(Log N) condition: Tree is balanced
    def insertNode(self,data,node):
        if data < node.data:
            if node.leftNode:
                self.insertNode(data,node.leftNode)
            else:
                node.leftNode=Node(data)
        else:
            if node.rightNode:
                self.insertNode(data,node.rightNode)
            else:
                node.rightNode=Node(data)
    
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
        
    def getMin(self,node):
        if node.leftNode:
            return self.getMin(node.leftNode)
        
        print(node.data)

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.rightNode:
            return self.getMax(node.rightNode)
        
        print(node.data)

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
        
    def traverseInOrder(self,node):
          
        if node.leftNode:
            self.traverseInOrder(node.leftNode)

        print("%s " % node.data)
        if node.rightNode:
            self.traverseInOrder(node.rightNode)

    def remove(self,data):
        if self.root:
            self.root=self.removeNode(data,self.root)
    
    def removeNode(self,data,node):
        if not node: 
            return node
        
        if data<node.data:
            node.leftNode= self.removeNode(data,node.leftNode)
        elif data>node.data:
            node.rightNode=self.removeNode(data,node.rightNode)
        else:
            
            if not node.leftNode and not node.rightNode:
                print("Removing a leaf Node")
                del node
                return None
            
            if not node.leftNode:
                print("Removing node with single right child")
                tempNode= node.rightNode
                del node
                return tempNode
            elif not node.rightNode:
                print("Removing node with single left child")
                tempNode= node.leftNode
                del node

            print("removing node with two children") 
            tempNode= self.getPredecessor(node.leftNode)
            node.data=tempNode.data
            node.leftNode=self.removeNode(tempNode.data,node.leftNode)

        return node

    def getPredecessor(self,node):
        if node.rightNode:
            return self.getPredecessor(node.rightNode)

        return node            
bst=BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(61)
bst.remove(61)
print(bst.getMinValue())
print(bst.traverse())