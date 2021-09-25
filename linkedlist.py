# LinkedList Using Classes 
# Linkedlist index is starting from 0
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        
    # method to add value at head
    def addhead(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length+=1
        return f"Value : {value} added to the head node of linkedlist"
    
    # method to add value at tail
    def push(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.length+=1
            return f"Value : {value} added at the head node of LinkedList"
        else:    
            
            self.tail.next = newNode
            self.tail = newNode
            self.length+=1
            return f"Value : {value} added at the end of node LinkedList"

    # method to insert value at anywhere in LinkedList
    def insert(self, index, value):
        if (index <=1):
            return self.addhead(value)
        elif (index > self.length):
            return self.push(value)
        else:
            newNode = Node(value)
            pre = self.interate(index-1)
            currentNode = pre.next
            newNode.next = currentNode
            pre.next = newNode
            self.length+=1
            return f"Value : {value} added at node : {index} of linkedlist"

    # method to iterate through linkedlist
    def interate(self,index):
        currentNode = self.head
        i = 0
        while(i<index):
            currentNode = currentNode.next
            i+=1
        return currentNode

    # method to traverse through all elements in the linkedlist
    def traverse(self):
        linkedlist = []
        if self.head == None:
            return linkedlist
        else:
            currentNode = self.head
            while(currentNode!=None):
                linkedlist.append(currentNode.value)
                currentNode = currentNode.next
        return f"List elements : {linkedlist}"

    def remove(self, index):
        if (index<=0):
            headNode = self.head
            self.head = self.head.next
            self.length-=1
            return f"value : {headNode.value} is deleted from linkedlist at index 0"
        elif(index>self.length-1):
            return f"Index is not present in linkedlist"
        else:    
            currentNode = self.interate(index)
            pre = self.interate(index-1)
            pre.next = currentNode.next
            self.length-=1
            return f"value : {currentNode.value} is deleted from linkedlist at index {index}"

mylist = LinkedList()
mylist.addhead(1)
mylist.addhead(2)
mylist.addhead(3)
mylist.addhead(4)
mylist.addhead(5)
mylist.push(8)  
print(mylist.insert(4,7))
print(mylist.traverse())
print(mylist.remove(4))
print(mylist.traverse())
print(mylist.length)
