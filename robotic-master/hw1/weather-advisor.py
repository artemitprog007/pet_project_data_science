def weather_advisor():
    """
    Задача: Дать рекомендации по одежде в зависимости от сезона и температуры
    """
    month = input("Введите месяц (числом 1-12 или словом): ").strip().lower()
    try:
        temp = float(input("Введите текущую температуру (°C): "))
    except ValueError:
        print("Ошибка: температура должна быть числом.")
        return

    # Определяем сезон
    seasons = {
        "зима": [12, 1, 2],
        "весна": [3, 4, 5],
        "лето": [6, 7, 8],
        "осень": [9, 10, 11],
    }

    # Перевод месяца в число
    months_map = {
        "январь": 1, "февраль": 2, "март": 3, "апрель": 4, "май": 5, "июнь": 6,
        "июль": 7, "август": 8, "сентябрь": 9, "октябрь": 10, "ноябрь": 11, "декабрь": 12
    }

    if month.isdigit():
        m = int(month)
    else:
        m = months_map.get(month, None)

    if not m or not (1 <= m <= 12):
        print("Ошибка: введите корректный месяц (1–12 или словом).")
        return

    # Определяем сезон по месяцу
    for season, months in seasons.items():
        if m in months:
            current_season = season
            break

    # Базовые рекомендации
    if temp < -10:
        advice = "Очень холодно: теплая куртка, шапка, шарф, перчатки"
        warning = "Осторожно! Возможен сильный мороз"
    elif temp < 5:
        advice = "Куртка, шапка, возможно перчатки"
        warning = "Будьте аккуратны: возможен гололёд"
    elif temp < 15:
        advice = "Легкая куртка или свитер"
        warning = None
    elif temp < 25:
        advice = "Футболка, лёгкая одежда"
        warning = None
    else:
        advice = "Очень жарко: лёгкая одежда, пить больше воды"
        warning = "Осторожно! Риск перегрева"

    # Вывод
    print(f"\nСейчас {current_season}, {temp}°C")
    print(f"Рекомендация: {advice}")
    if warning:
        print(warning)


# Вызов функции
weather_advisor()
