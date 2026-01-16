def number_sequence_analyzer():
    """
    Задача: Проанализировать последовательность чисел
    """
    numbers = []

    print("Введите числа по одному. Для завершения введите 'stop'.")
    while True:
        value = input("> ").strip().lower()
        if value == "stop":
            break
        try:
            numbers.append(float(value))
        except ValueError:
            print("Ошибка: введите число или 'stop'.")

    if not numbers:
        print("Последовательность пуста.")
        return

    count = len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / count

    # Проверка на дубли
    has_duplicates = len(numbers) != len(set(numbers))

    # Сортировка и медиана
    sorted_nums = sorted(numbers)
    mid = count // 2
    if count % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]

    # Простейший график (масштабируем к 10 символам)
    scale = max(numbers)
    graph = "".join("█" * int((n / scale) * 10) if scale > 0 else "▁" for n in numbers)

    # Вывод
    print(f"\nЧисел введено: {count}")
    print(f"Максимум: {maximum}, Минимум: {minimum}, Среднее: {average:.2f}")
    print(f"Медиана: {median}")
    print("Есть ли повторяющиеся числа:", "Да" if has_duplicates else "Нет")
    print(f"График: {graph}")


# Вызов функции
number_sequence_analyzer()
