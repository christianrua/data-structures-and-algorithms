

from ast import Nonlocal


class Node():

    def __init__(self, value, type='not-dict'):
        if type == 'not-dict':
            self.value = value
            self.left = None
            self.right = None
        else:
            self.dict = {
                "value":value,
                "left":None,
                "right":None
            }

    def __repr__(self) -> str:
        return str(self.dict)        
