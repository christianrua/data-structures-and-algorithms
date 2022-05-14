"The Chair Interface"
from abc import ABCMeta, abstractmethod


class IQueue(metaclass=ABCMeta):
    "The Stack Interface"

    @staticmethod
    @abstractmethod
    def peek():
        """
            Shows the top node of the queue
        """
        pass

    @staticmethod    
    @abstractmethod    
    def enqueue():
        """
            Adds a Node at the tail of the queue
        """
        pass

    @staticmethod       
    @abstractmethod  
    def dequeue():
        """
            Remove from the head of the quee
        """   
        pass
