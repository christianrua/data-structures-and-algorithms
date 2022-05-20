from queue_interface import IQueue
from node import Node

class Queue(IQueue):

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def _print_status(self):
        print(f"current length {self.length}")
        print(f"current first {self.first.value}") 
        if (self.last != None):   
            print(f"current last {self.last.value}")     

    def peek(self):
        return self.first

    def enqueue(self, value):
        """
            Adds a Node at the tail of the queue
        """
        node = Node(value)
        if(self.first == None):
            self.first = node
            self.last = node
            self.length += 1
            
        else: 
            new_node = node
            self.last.next = new_node
            self.last = new_node
            self.length += 1

        self._print_status()  

    def dequeue(self):

        if self.first == None:
            return None

        current_node = self.first
        self.first = current_node.next
        self.length -= 1

        self._print_status()

        return current_node

         

    def __repr__(self) -> str:
        return str(self)          


queue = Queue()
print("adding")
queue.enqueue("Nastiness")
print("adding")
queue.enqueue("Doomsday")
print("adding")
queue.enqueue("Merciless Death")
print("decreasing")
print(queue.dequeue().value)
print("decreasing")
print(queue.dequeue().value)






