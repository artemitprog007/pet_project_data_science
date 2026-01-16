import threading
import queue
import time
import random

product_types = ["еда", "одежда", "электроника"]
producers_config = [
    {"name": "Фабрика-А", "type": "еда", "count": 3},
    {"name": "Фабрика-Б", "type": "одежда", "count": 4},
    {"name": "Фабрика-В", "type": "электроника", "count": 2}
]

def producer(q, name, product_type, count):
    """Производитель товаров"""
    for i in range(count):
        item = f"{product_type} от {name}-{i}"
        q.put(item)
        print(f"🛠️ {name} произвел: {item}")
        time.sleep(random.uniform(0.1, 0.4))
    q.put(None)  # сигнал о завершении

def consumer(q, name):
    """Потребитель"""
    while True:
        item = q.get()
        if item is None:
            q.put(None)  # передаем сигнал дальше
            break
        print(f"🛒 {name} купил: {item}")
        time.sleep(random.uniform(0.2, 0.6))
        q.task_done()

# Очередь
q = queue.Queue()

# Создаем производителей по конфигу
producers = []
for config in producers_config:
    t = threading.Thread(
        target=producer,
        args=(q, config["name"], config["type"], config["count"])
    )
    producers.append(t)

# Создаем потребителей
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

print("🎉 Все продукты произведены и распроданы!")
