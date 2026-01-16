def report_generator():
    """
    Задача: Сгенерировать отчет по продажам
    """
    sales_data = [
        {"product": "Ноутбук", "price": 50000, "quantity": 3},
        {"product": "Мышь", "price": 1500, "quantity": 10},
        {"product": "Клавиатура", "price": 3000, "quantity": 5},
        {"product": "Монитор", "price": 20000, "quantity": 2}
    ]

    # Общая выручка
    total_revenue = sum(item["price"] * item["quantity"] for item in sales_data)

    # Самый продаваемый товар (по количеству)
    best_selling = max(sales_data, key=lambda x: x["quantity"])

    # Товар с максимальной выручкой
    max_revenue_item = max(sales_data, key=lambda x: x["price"] * x["quantity"])

    # Средний чек (средняя стоимость покупки одного товара)
    total_items = sum(item["quantity"] for item in sales_data)
    average_check = total_revenue / total_items if total_items else 0

    # Отчёт
    print("=== ОТЧЕТ О ПРОДАЖАХ ===")
    print(f"Общая выручка: {total_revenue:,.0f} руб.")
    print(f"Самый продаваемый товар: {best_selling['product']} ({best_selling['quantity']} шт.)")
    print(f"Товар с макс. выручкой: {max_revenue_item['product']} "
          f"({max_revenue_item['price'] * max_revenue_item['quantity']:,.0f} руб.)")
    print(f"Средний чек: {average_check:,.0f} руб.")


# Вызов функции
report_generator()
