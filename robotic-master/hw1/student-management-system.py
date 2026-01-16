def student_management_system():
    """
    Мини-система для управления данными студентов
    """
    students = []

    while True:
        print("\n=== СИСТЕМА УПРАВЛЕНИЯ СТУДЕНТАМИ ===")
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Найти студента по имени")
        print("4. Рассчитать средний балл группы")
        print("5. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Имя: ").strip()
            try:
                age = int(input("Возраст: "))
                grades_raw = input("Оценки через пробел: ").split()
                grades = [float(g) for g in grades_raw] if grades_raw else []
                students.append({"name": name, "age": age, "grades": grades})
                print(f"Студент {name} добавлен.")
            except ValueError:
                print("Ошибка: возраст и оценки должны быть числами.")

        elif choice == "2":
            if not students:
                print("Список студентов пуст.")
            else:
                print("\nСписок студентов:")
                print("{:<15} {:<5} {:<20}".format("Имя", "Возраст", "Оценки"))
                for s in students:
                    grades_str = " ".join(map(str, s["grades"])) if s["grades"] else "-"
                    print("{:<15} {:<5} {:<20}".format(s["name"], s["age"], grades_str))

        elif choice == "3":
            search = input("Введите имя для поиска: ").strip().lower()
            found = [s for s in students if s["name"].lower() == search]
            if found:
                for s in found:
                    print(f"Имя: {s['name']}, Возраст: {s['age']}, Оценки: {s['grades']}")
            else:
                print("Студент не найден.")

        elif choice == "4":
            all_grades = [g for s in students for g in s["grades"]]
            if all_grades:
                avg = sum(all_grades) / len(all_grades)
                print(f"Средний балл группы: {avg:.2f}")
            else:
                print("Оценок пока нет.")

        elif choice == "5":
            print("Выход из системы...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


# Вызов функции
student_management_system()
