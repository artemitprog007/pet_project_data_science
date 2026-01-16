class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Пример использования
root = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")

root.add_child(b)
root.add_child(c)
b.add_child(d)

print(root)
# A
#   B
#     D
#   C