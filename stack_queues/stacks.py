from stack_interface import IStack

from node import Node

class Stack(IStack):

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0 

    def peek(self):
        """
            Shows the top node
        """
        return self.top
        

    def push(self, value):
        """
            Adds a Node at the top of the stack
        """
        node = Node(value)
        if self.top != None:
            self.bottom = self.top
            self.top = node
            node.next = self.bottom
            self.length += 1
        else:
            self.top = node
            node.next = self.bottom
            self.length += 1
           

    def pop(self):
        """
            Remove from the top of the stack
        """   
        if self.bottom == None:
            return None  
            
        head = self.top
        self.top = self.bottom 
        self.length =- 1
        return head

    def __repr__(self) -> str:
        return str(self)    
    

my_stack = Stack()    
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
print(my_stack.peek().value)
some_node = my_stack.pop()
print("detach element",some_node.value)
print("actual head",my_stack.peek().value)


