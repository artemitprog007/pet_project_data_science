import threading
import time

# Цвета ANSI
colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m"]  # красный, зеленый, желтый, синий
reset_color = "\033[0m"

def print_numbers(color, thread_id):
    """Печатает числа"""
    for i in range(5):
        print(f"{color}Поток-{thread_id}: число {i}{reset_color}")
        time.sleep(1)
    print(f"{color}Поток-{thread_id} завершен!{reset_color}")

def print_letters(color, thread_id):
    """Печатает буквы"""
    for letter in 'ABCDE':
        print(f"{color}Поток-{thread_id}: буква {letter}{reset_color}")
        time.sleep(1)
    print(f"{color}Поток-{thread_id} завершен!{reset_color}")

# Создаем 4 потока
threads = []
threads.append(threading.Thread(target=print_numbers, args=(colors[0], 1)))
threads.append(threading.Thread(target=print_letters, args=(colors[1], 2)))
threads.append(threading.Thread(target=print_numbers, args=(colors[2], 3)))
threads.append(threading.Thread(target=print_letters, args=(colors[3], 4)))

# Запускаем все
for t in threads:
    t.start()

# Ждем завершения
for t in threads:
    t.join()

print("🎉 Все потоки завершили работу!")
