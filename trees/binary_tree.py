
from node_class import Node

class BinarySeachTree():
    
    def __init__(self):
        self.root = None
        self.tree_nodes = []

    def _append_node(self, node):
        self.tree_nodes.append(node)

    def _check_none_value(self, node):
        if node == None:
            return "none value"
        else:
            return node.value        

    def insert(self, value):

        node = Node(value)
        if self.root == None:
            self.root = node
            self._append_node(node)
        else:
            current_node = self.root
            while current_node:
                if value > current_node.value:
                    if current_node.right == None:
                        current_node.right = node
                        self._append_node(node)
                        break 
                    else:
                        current_node = current_node.right  
                else:
                    if current_node.left == None:
                        current_node.left = node
                        self._append_node(node)
                        break 
                    else:
                        current_node = current_node.left 

    def lookup(self, value):
        pass

    def remove(self, value):
        pass

    def print_tree(self):
        for node in self.tree_nodes:
            print(f"node value: {node.value}, node left value {self._check_none_value(node.left)}, node right {self._check_none_value(node.right)}")  
      

binary_tree = BinarySeachTree()
binary_tree.insert(5)
binary_tree.insert(10)
binary_tree.insert(2)
binary_tree.insert(11)
binary_tree.insert(15)
binary_tree.print_tree()
