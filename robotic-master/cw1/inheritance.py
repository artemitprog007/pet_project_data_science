# Родительский класс
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Животное издает звук"

# Дочерний класс
class Cat(Animal):  # Cat наследует от Animal
    def speak(self):
        return f"{self.name} говорит: Мяу!"

class Dog(Animal):  # Dog наследует от Animal
    def speak(self):
        return f"{self.name} говорит: Гав!"

# Использование
cat = Cat("Мурка")
dog = Dog("Бадди")

print(cat.speak())  # Мурка говорит: Мяу!
print(dog.speak())  # Бадди говорит: Гав!