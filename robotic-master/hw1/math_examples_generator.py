def math_examples_generator():
    """
    Задача: Сгенерировать и решить случайные математические примеры
    """
    import random
    import operator

    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv  # используем целочисленное деление для простоты
    }

    score = 0
    total = 10

    print("=== Тест из 10 примеров ===")
    for i in range(1, total + 1):
        op = random.choice(list(operations.keys()))
        a = random.randint(1, 20)
        b = random.randint(1, 20)

        # чтобы не делить на ноль
        if op == "/":
            b = random.randint(1, 20)

        correct = operations[op](a, b)

        try:
            user_answer = int(input(f"{i}. {a} {op} {b} = "))
            if user_answer == correct:
                print("✅ Верно")
                score += 1
            else:
                print(f"❌ Неверно (правильный ответ: {correct})")
        except ValueError:
            print(f"❌ Ошибка ввода (правильный ответ: {correct})")

    percent = score / total * 100
    print(f"\nРезультат: {score}/{total} правильных ответов ({percent:.0f}%)")


# Вызов функции
math_examples_generator()
