def caesar_cipher():
    """
    Реализация шифра Цезаря: шифрование и дешифрование текста
    """
    text = input("Введите текст: ")
    try:
        shift = int(input("Введите сдвиг (например, 3): "))
    except ValueError:
        print("Ошибка: сдвиг должен быть числом.")
        return

    mode = input("Выберите режим (e — зашифровать, d — расшифровать): ").strip().lower()
    if mode not in ("e", "d"):
        print("Ошибка: выберите 'e' или 'd'.")
        return

    if mode == "d":
        shift = -shift

    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(ch)

    action = "Зашифровано" if mode == "e" else "Расшифровано"
    print(f"{action}: {''.join(result)}")


# Вызов функции
caesar_cipher()
