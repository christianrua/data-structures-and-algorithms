from stack_interface import IStack
from sqlalchemy import null

class Node():

    def __init__(self, value):
        self.value = value
        self.next = null

class Stack(IStack):

    def __init__(self):
        self._array = []
         

    def peek(self):
        """
            Shows the top node
        """
        return self._array[0]
        

    def push(self, value):
        """
            Adds a Node at the top of the stack
        """
        node = Node(value)
        
        #if self.top != None:
        if self._array != []:    
            node.next = self._array[0]
            self._array.insert(0, node)
            
        else:
            self._array.append(node)

    def pop(self):
        """
            Remove from the top of the stack
        """   
        return self._array.pop(0)

    def __repr__(self) -> str:
        return str(self)    
    

my_stack = Stack()    
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
print(f"this is the head {my_stack.peek().value}")
some_node = my_stack.pop()
print("detach element",some_node.value)
print("actual head",my_stack.peek().value)