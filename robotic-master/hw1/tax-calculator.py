def tax_calculator():
    """
    Задача: Рассчитать налог в зависимости от дохода
    """
    try:
        income = float(input("Введите годовой доход (руб): "))

        if income <= 15000:
            tax_rate = 0.0
        elif income <= 50000:
            tax_rate = 0.15
        elif income <= 100000:
            tax_rate = 0.25
        else:
            tax_rate = 0.30

        tax = income * tax_rate
        net_income = income - tax

        print(f"\nНалог: {tax:,.2f} руб.")
        print(f"Чистый доход: {net_income:,.2f} руб.")

    except ValueError:
        print("Ошибка: введите корректное число!")


# Вызов функции
tax_calculator()
