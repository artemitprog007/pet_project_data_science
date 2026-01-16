import threading
import time

# Цвета ANSI
colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m"]
reset_color = "\033[0m"

start_number = 5
letters = "EDCBA"

def print_numbers(color, thread_id, start_number):
    """Обратный отсчет чисел"""
    for i in range(start_number, 0, -1):
        print(f"{color}Поток-{thread_id}: число {i}{reset_color}")
        time.sleep(1)
    print(f"{color}Поток-{thread_id} завершен!{reset_color}")

def print_letters(color, thread_id, letters):
    """Обратный порядок букв"""
    for letter in letters:
        print(f"{color}Поток-{thread_id}: буква {letter}{reset_color}")
        time.sleep(1)
    print(f"{color}Поток-{thread_id} завершен!{reset_color}")

# Создаем 4 потока
threads = []
threads.append(threading.Thread(target=print_numbers, args=(colors[0], 1, start_number)))
threads.append(threading.Thread(target=print_letters, args=(colors[1], 2, letters)))
threads.append(threading.Thread(target=print_numbers, args=(colors[2], 3, start_number)))
threads.append(threading.Thread(target=print_letters, args=(colors[3], 4, letters)))

# Запускаем все потоки
for t in threads:
    t.start()

# Ждем завершения
for t in threads:
    t.join()

print("🎉 Все потоки завершили работу!")
