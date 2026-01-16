def financial_calculator():
    """
    Задача: Рассчитать сложные проценты по вкладу
    """
    import math

    try:
        principal = float(input("Введите начальную сумму (руб): "))
        rate = float(input("Введите процентную ставку годовых (%): ")) / 100
        years = int(input("Введите срок вклада (лет): "))
        target = float(input("Введите целевую сумму (руб): "))

        if principal <= 0 or rate < 0 or years < 0 or target <= 0:
            print("Ошибка: значения должны быть положительными!")
            return

        # Формула сложных процентов (капитализация 1 раз в год)
        final_amount = principal * (1 + rate) ** years

        print(f"\nЧерез {years} лет: {final_amount:.2f} руб.")
        print(f"Цель {target:.2f} руб. достигнута: {final_amount >= target}")

        # Расчёт срока удвоения
        if rate == 0:
            print("При нулевой ставке сумма никогда не удвоится.")
        else:
            doubling_time = math.log(2) / math.log(1 + rate)
            print(f"Сумма удвоится примерно через {math.ceil(doubling_time)} лет "
                  f"(точно: {doubling_time:.2f})")

    except ValueError:
        print("Ошибка: введите корректные числовые значения!")


# Вызов функции
financial_calculator()
