import sys

NODE_TYPE_ROOT = 'root'
NODE_TYPE_LEFT = 'left'
NODE_TYPE_RIGHT = 'right'

class Node:
    def __init__(self, node_data):
        self.left_node = None
        self.right_node = None
        self.parent_node = None
        self.node_type = None
        self.node_layer = None
        self.node_data = node_data

class Tree:
    def __init__(self):
        self.total_nodes = 0


class BST(Tree):
    def __init__(self):
        super().__init__()
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            new_node.node_layer = 0
            new_node.node_type = NODE_TYPE_ROOT
            self.root = new_node
        else:
            self.recursive_insert(new_node, self.root)            

    def recursive_insert(self, new_node, parent_node):
        if new_node.node_data > parent_node.node_data:
            self.insert_right(new_node, parent_node)
        elif new_node.node_data < parent_node.node_data:
            self.insert_left(new_node, parent_node)
        else:
            self.insert_right(new_node, parent_node)

    def insert_right(self, new_node, parent_node):
        if parent_node.right_node is None:
            new_node.node_layer = parent_node.node_layer + 1
            new_node.node_type = NODE_TYPE_RIGHT
            parent_node.right_node = new_node
        else:
            self.recursive_insert(new_node, parent_node.right_node)

    def insert_left(self, new_node, parent_node):
        if parent_node.left_node is None:
            new_node.node_layer = parent_node.node_layer + 1
            new_node.node_type = NODE_TYPE_LEFT
            parent_node.left_node = new_node
        else:
            self.recursive_insert(new_node, parent_node.left_node)

    def in_order_traversal(self):
        if self.root is None:
            return
        else:
            self.in_order_traversal_recursive(self.root, '')

    def in_order_traversal_recursive(self, current_node, builder):
        if current_node.left_node is not None:
            self.in_order_traversal_recursive(current_node.left_node , builder + '  ')
        self.print_node_stats(current_node)
        if current_node.right_node is not None:
            self.in_order_traversal_recursive(current_node.right_node, builder + '  ')

    def print_node_stats(self, node):
        print("Data: " + str(node.node_data))
        print("Type: " + node.node_type)
        print("Layer: " + str(node.node_layer))
        print("Parent Node: " + str(node.parent_node))
        print("Left Child: " + str(node.left_node))
        print("RIght Child: " + str(node.right_node))
        

        
T = BST()
T.insert(1)
T.insert(2)
T.insert(7)
T.insert(4)
T.insert(5)
T.in_order_traversal()

array = [3,2,4,1,5]


for item in array:
    print(str(' ' * len(array)) + str(item))


#                   3
#       ____________|____________
#      /                         \
#     2                           4
#     |

#   1
#   |
#  / \