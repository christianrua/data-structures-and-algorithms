
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

    def traverse(self, node,tree={},level=0, type="root"):
        tree[f"node {level} {type} value"] = node.value
        
        if node.left != None:
            self.traverse(node.left, tree, level + 1, "left")    
        else:
            tree[f"node {level + 1} left value"] = None
            return tree

        if node.right != None:
            self.traverse(node.right,tree, level + 1, "right")
        else:
            tree[f"node {level + 1} right value"] = None
            return tree    

        return tree     

    def print_tree_2(self):
        tree = self.traverse(self.root)    
        


      

binary_tree = BinarySeachTree()
binary_tree.insert(9)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(20)
binary_tree.insert(170)
binary_tree.insert(15)
binary_tree.insert(1)
binary_tree.print_tree()
print(binary_tree.traverse(binary_tree.root))

