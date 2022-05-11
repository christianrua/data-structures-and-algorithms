"The Chair Interface"
from abc import ABCMeta, abstractmethod


class IStack(metaclass=ABCMeta):
    "The Stack Interface"

    @staticmethod
    @abstractmethod
    def peek():
        """
            Shows the top node
        """
        pass

    @staticmethod    
    @abstractmethod    
    def push():
        """
            Adds a Node at the top of the stack
        """
        pass

    @staticmethod       
    @abstractmethod  
    def pop():
        """
            Remove from the top of the stack
        """   
        pass

    # @staticmethod       
    # @abstractmethod  
    # def lenght():
    #     """
    #         Return the lenght of the stack
    #     """
    #     pass