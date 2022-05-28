
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

    def insert_v2(self, value):

        node = Node(value, type="dict")
        if self.root == None:
            self.root = node
            self._append_node(node)
        else:
            current_node = self.root
            while current_node:
                if value > current_node.dict["value"]:
                    if current_node.dict["right"] == None:
                        current_node.dict["right"] = node
                        self._append_node(node)
                        break 
                    else:
                        current_node = current_node.dict["right"]  
                else:
                    if current_node.dict["left"] == None:
                        current_node.dict["left"] = node
                        self._append_node(node)
                        break 
                    else:
                        current_node = current_node.dict["left"]           

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
            tree[f"node {level + 1} left value"] = node.value
            return tree

        if node.right != None:
            self.traverse(node.right,tree, level + 1, "right")
        else:
            tree[f"node {level + 1} right value"] = node.value
            return tree    

        return tree     

    def print_tree_v2(self):
        """
        Make the print statement over this json
        {'value': 9, 
        'left': {'value': 4, 
                'left': {'value': 1, 
                        'left': None, 
                        'right': None
                        }, 
                'right': {'value': 6, 
                        'left': None, 
                        'right': None
                        }
                }, 
        'right': {'value': 20, 
                'left': {'value': 15, 
                        'left': None, 
                        'right': None}, 
                right': {'value': 170, 
                        'left': None, 
                        'right': None
                        }
                }
        }
        """
        print(self.root)    
        


      

binary_tree = BinarySeachTree()
# binary_tree.insert(9)
# binary_tree.insert(4)
# binary_tree.insert(6)
# binary_tree.insert(20)
# binary_tree.insert(170)
# binary_tree.insert(15)
# binary_tree.insert(1)
# binary_tree.print_tree()
# print(binary_tree.traverse(binary_tree.root))

binary_tree.insert_v2(9)
binary_tree.insert_v2(4)
binary_tree.insert_v2(6)
binary_tree.insert_v2(20)
binary_tree.insert_v2(170)
binary_tree.insert_v2(15)
binary_tree.insert_v2(1)
binary_tree.print_tree_v2()

