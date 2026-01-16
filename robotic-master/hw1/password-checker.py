def password_checker():
    """
    Проверка пароля на надежность:
    - длина >= 8
    - содержит цифры
    - содержит заглавные и строчные буквы
    - содержит спецсимволы
    """
    import string

    password = input("Введите пароль для проверки: ")

    # Условия
    has_length = len(password) >= 8
    has_digit = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)

    # Проверка
    print("\nРезультаты проверки:")
    print(f"- Длина >= 8: {'OK' if has_length else 'Нет'}")
    print(f"- Есть цифра: {'OK' if has_digit else 'Нет'}")
    print(f"- Есть заглавная буква: {'OK' if has_upper else 'Нет'}")
    print(f"- Есть строчная буква: {'OK' if has_lower else 'Нет'}")
    print(f"- Есть спецсимвол: {'OK' if has_special else 'Нет'}")

    # Итог
    if all([has_length, has_digit, has_upper, has_lower, has_special]):
        print("\nПароль надежный ✅")
    else:
        print("\nПароль слабый ❌")


# Вызов функции
password_checker()
