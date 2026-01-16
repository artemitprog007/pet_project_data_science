def atm_simulator():
    """
    Упрощённая симуляция работы банкомата
    """
    balance = 10000  # начальный баланс
    limit = 5000     # лимит на снятие за одну операцию

    while True:
        print("\n=== БАНКОМАТ ===")
        print(f"Текущий баланс: {balance} руб.")
        print("1. Показать баланс")
        print("2. Снять наличные")
        print("3. Пополнить счет")
        print("4. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            print(f"Ваш баланс: {balance} руб.")

        elif choice == "2":
            try:
                amount = int(input("Сумма для снятия: "))
                if amount <= 0:
                    print("Ошибка: сумма должна быть положительной.")
                elif amount % 100 != 0:
                    print("Ошибка: сумма должна быть кратна 100.")
                elif amount > balance:
                    print("Ошибка: недостаточно средств.")
                elif amount > limit:
                    print(f"Ошибка: лимит снятия {limit} руб. за одну операцию.")
                else:
                    balance -= amount
                    print(f"Снято {amount} руб. Остаток: {balance} руб.")
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "3":
            try:
                amount = int(input("Сумма пополнения: "))
                if amount <= 0:
                    print("Ошибка: сумма должна быть положительной.")
                elif amount % 100 != 0:
                    print("Ошибка: сумма должна быть кратна 100.")
                else:
                    balance += amount
                    print(f"Счёт пополнен на {amount} руб. Баланс: {balance} руб.")
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "4":
            print("Спасибо за использование банкомата. До свидания!")
            break

        else:
            print("Ошибка: выберите пункт меню от 1 до 4.")


# Вызов функции
atm_simulator()
