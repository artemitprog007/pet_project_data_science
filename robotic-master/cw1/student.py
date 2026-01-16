class Student:
    university = "Python University"
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # список оценок
    
    def add_grade(self, grade):
        """Добавить оценку"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return f"Оценка {grade} добавлена"
        else:
            return "Оценка должна быть от 0 до 100"
    
    def get_average(self):
        """Посчитать средний балл"""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
    
    def get_info(self):
        """Получить информацию о студенте"""
        return f"Студент: {self.name}, ID: {self.student_id}, Средний балл: {self.get_average():.2f}"

# Использование
student1 = Student("Анна", "S001")
student2 = Student("Михаил", "S002")

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(90)
student2.add_grade(88)

print(student1.get_info())  # Студент: Анна, ID: S001, Средний балл: 85.00
print(student2.get_info())  # Студент: Михаил, ID: S002, Средний балл: 89.00