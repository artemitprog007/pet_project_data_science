import threading
from queue import PriorityQueue
import time
import random

# Приоритеты: чем меньше число — тем выше приоритет
priority_map = {"еда": 1, "электроника": 2, "одежда": 3}

producers_config = [
    {"name": "Фабрика-А", "type": "еда", "count": 3},
    {"name": "Фабрика-Б", "type": "одежда", "count": 4},
    {"name": "Фабрика-В", "type": "электроника", "count": 2}
]

def producer(q, name, product_type, count):
    """Производитель товаров с приоритетом"""
    for i in range(count):
        item = f"{product_type} от {name}-{i}"
        q.put((priority_map[product_type], item))  # кладем кортеж (приоритет, товар)
        print(f"🛠️ {name} произвел: {item} (приоритет {priority_map[product_type]})")
        time.sleep(random.uniform(0.1, 0.4))
    q.put((priority_map[product_type], None))  # сигнал завершения

def consumer(q, name):
    """Потребитель"""
    while True:
        priority, item = q.get()
        if item is None:
            q.put((priority, None))  # передаем сигнал дальше
            break
        print(f"🛒 {name} купил: {item} (приоритет {priority})")
        time.sleep(random.uniform(0.2, 0.6))
        q.task_done()

# Очередь с приоритетами
q = PriorityQueue()

# Производители
producers = []
for config in producers_config:
    t = threading.Thread(
        target=producer,
        args=(q, config["name"], config["type"], config["count"])
    )
    producers.append(t)

# Потребители
consumers = [
    threading.Thread(target=consumer, args=(q, "Магазин-1")),
    threading.Thread(target=consumer, args=(q, "Магазин-2"))
]

# Запуск
for p in producers: p.start()
for c in consumers: c.start()

# Синхронизация
for p in producers: p.join()
q.join()

print("🎉 Все продукты произведены и распроданы с учетом приоритетов!")
