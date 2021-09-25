# Stacks using linkedlist
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    if self.top == None:
      return None
    else:
      return self.top.value

  def push(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.top = newNode
      self.bottom = newNode
    else:
      holdingPointer = self.top
      self.top = newNode
      self.top.next = holdingPointer
    
    self.length+=1
    return f"pushed {value} in stack"
  
  def pop(self):
    if (self.top == None): 
      return None
    else:
      holdingPointer = self.top
      self.top = self.top.next
      self.length-=1
      return f"popped {holdingPointer.value} from stack"


mystack = Stack()

print(mystack.push(23))
print(mystack.push(43))
print(mystack.push(56))
print(mystack.pop())
print(mystack.pop())
print(mystack.peek())