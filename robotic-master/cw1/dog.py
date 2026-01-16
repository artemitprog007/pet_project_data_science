class Dog:
    # Классовый атрибут - общий для ВСЕХ собак
    species = "Canis familiaris"
    total_dogs = 0  # счетчик всех созданных собак
    
    def __init__(self, name, age):
        # Атрибуты экземпляра - уникальные для КАЖДОЙ собаки
        self.name = name
        self.age = age
        Dog.total_dogs += 1  # увеличиваем счетчик при создании каждой собаки

# Создаем несколько собак
dog1 = Dog("Бадди", 3)
dog2 = Dog("Чарли", 5)

print(dog1.species)        # Canis familiaris
print(dog2.species)        # Canis familiaris
print(Dog.total_dogs)      # 2 (создали двух собак)

# Меняем классовый атрибут
Dog.species = "Собака"
print(dog1.species)        # Собака (изменилось у всех!)
print(dog2.species)        # Собака

# Меняем атрибут экземпляра
dog1.name = "Макс"
print(dog1.name)           # Макс (изменилось только у dog1)
print(dog2.name)           # Чарли (не изменилось)