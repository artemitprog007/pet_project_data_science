class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Вставка значения в дерево"""
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = BSTNode(value)
                current.left.parent = current
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = BSTNode(value)
                current.right.parent = current
            else:
                self._insert_recursive(current.right, value)
    
    def search(self, value):
        """Поиск значения в дереве"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)
    
    def find_min(self, node=None):
        """Нахождение минимального значения"""
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node.value
    
    def find_max(self, node=None):
        """Нахождение максимального значения"""
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node.value
    
    def delete(self, value):
        """Удаление значения из дерева"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, current, value):
        if current is None:
            return current
        
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Узел с одним или без детей
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            
            # Узел с двумя детьми: находим минимальный в правом поддереве
            min_node = self._find_min_node(current.right)
            current.value = min_node.value
            current.right = self._delete_recursive(current.right, min_node.value)
        
        return current
    
    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def display(self):
        """Визуализация дерева"""
        if self.root:
            self._display_recursive(self.root)
    
    def _display_recursive(self, node, level=0, prefix="Root: "):
        if node:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left or node.right:
                if node.left:
                    self._display_recursive(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self._display_recursive(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

# Пример использования
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.insert(value)

print("Дерево:")
bst.display()
print(f"Минимальное значение: {bst.find_min()}")
print(f"Максимальное значение: {bst.find_max()}")
print(f"Поиск 40: {bst.search(40)}")
print(f"Поиск 100: {bst.search(100)}")