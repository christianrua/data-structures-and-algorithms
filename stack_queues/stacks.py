

from sqlalchemy import null


class Node():

    def __init__(self, value):
        self.value = value
        self.next = null

class Stack():

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
        if self.top != None:
            node = Node(value)
            self.bottom = self.top
            self.top = node
            node.next = self.bottom
            self.length += 1
        else:
            node = Node(value)
            self.top = node
            node.next = self.bottom
            self.length += 1

    def pop(self):
        """
            Remove from the top of the stack
        """     
        head = self.top
        self.top = self.bottom 
        self.length =- 1
        return head
    

my_stack = Stack()    
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
print(my_stack.peek().value)
some_node = my_stack.pop()
print("detach element",some_node.value)
print("actual head",my_stack.peek().value)


