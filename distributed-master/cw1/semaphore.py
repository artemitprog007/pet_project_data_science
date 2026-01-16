import threading
import time
import random

semaphore = threading.Semaphore(3)

def worker(worker_id):
    """Функция рабочего потока"""
    print(f"Работник {worker_id} ждет доступа...")
    
    semaphore.acquire()
    
    try:
        print(f"Работник {worker_id} получил доступ!")
        time.sleep(random.uniform(1, 3)) # критическая операциЯ
        print(f"Работник {worker_id} завершил работу.")
    finally:
        semaphore.release()
        print(f"Работник {worker_id} освободил доступ.")

threads = []
for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    print(f"Добавляю поток {t} в список")
    threads.append(t)
    t.start()

for t in threads:
    print(f"Поток {t} завершен")
    t.join()

print("Все работы завершены!")