def temperature_converter():
    """
    Конвертер между Цельсием (C), Фаренгейтом (F) и Кельвином (K).

    Формат ввода: "<число> <шкала>"
    Примеры: "25 C", "300 K", "-40 F"
    """
    raw = input("Введите температуру и шкалу (например, '25 C'): ").strip()

    try:
        value_str, scale = raw.split()
        t = float(value_str)
        scale = scale.upper()
        if scale not in {"C", "F", "K"}:
            print("Ошибка: шкала должна быть C, F или K")
            return

        # Переводим во внутренний базис — Кельвины
        if scale == "C":
            k = t + 273.15
        elif scale == "F":
            k = (t - 32) * 5/9 + 273.15
        else:  # "K"
            k = t

        # Физика не даст соврать
        if k < 0:
            print("Ошибка: ниже абсолютного нуля (0 K). Проверьте ввод.")
            return

        c = k - 273.15
        f = c * 9/5 + 32

        print(f"{c:.2f}°C = {f:.2f}°F = {k:.2f}K")

    except ValueError:
        print("Формат ввода: число и буква шкалы через пробел, например: 25 C")

temperature_converter()