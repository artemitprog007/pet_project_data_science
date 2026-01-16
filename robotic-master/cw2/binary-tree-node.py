class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"Node({self.value})"

class BinaryTree:
    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)
    
    def insert_left(self, parent, value):
        """Вставка в левое поддерево"""
        if parent.left is None:
            parent.left = BinaryTreeNode(value)
        else:
            new_node = BinaryTreeNode(value)
            new_node.left = parent.left
            parent.left = new_node
    
    def insert_right(self, parent, value):
        """Вставка в правое поддерево"""
        if parent.right is None:
            parent.right = BinaryTreeNode(value)
        else:
            new_node = BinaryTreeNode(value)
            new_node.right = parent.right
            parent.right = new_node
    
    def display(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left:
            self.display(node.left, level + 1, "L--- ")
        if node.right:
            self.display(node.right, level + 1, "R--- ")

# Пример
tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

tree.display()
# Root: 1
#     L--- 2
#         L--- 4
#         R--- 5
#     R--- 3