def list_calculator():
    """
    Задача: Выполнить различные операции со списком чисел
    """
    numbers = [12, 45, 23, 67, 34, 89, 56]
    print("Исходный список:", numbers)

    # Сумма всех элементов
    total = sum(numbers)

    # Среднее значение
    average = total / len(numbers)

    # Новый список с квадратами чисел
    squares = [x ** 2 for x in numbers]

    # Отфильтрованные числа > 30
    filtered = [x for x in numbers if x > 30]

    # Сортировка по убыванию
    sorted_desc = sorted(numbers, reverse=True)

    # Вывод результатов
    print(f"Сумма элементов: {total}")
    print(f"Среднее значение: {average:.2f}")
    print(f"Квадраты чисел: {squares}")
    print(f"Числа больше 30: {filtered}")
    print(f"Список по убыванию: {sorted_desc}")


# Вызов функции
list_calculator()
