class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Вычислить площадь"""
        return self.width * self.height
    
    def perimeter(self):
        """Вычислить периметр"""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}"


rect = Rectangle(5, 3)
print(rect)             # Прямоугольник 5x3
print("Площадь:", rect.area())       # 15
print("Периметр:", rect.perimeter()) # 16
