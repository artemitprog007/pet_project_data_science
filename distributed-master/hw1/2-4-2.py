import threading
import time
import random

# Ограничение: не более 3 файлов качаются одновременно
max_simultaneous_downloads = 3
download_semaphore = threading.Semaphore(max_simultaneous_downloads)

# Всего файлов для подсчёта
files = [
    ("document.pdf", 2.5),
    ("image.jpg", 1.8),
    ("video.mp4", 3.0),
    ("music.mp3", 2.2),
    ("archive.zip", 2.7)
]

active_downloads_lock = threading.Lock()
active_downloads = 0

def download_file(filename, size):
    global active_downloads

    with download_semaphore:  # гарантируем, что не больше 3 одновременных
        with active_downloads_lock:
            active_downloads += 1
            print(f"📥 Начата загрузка: {filename} (сейчас {active_downloads}/{max_simultaneous_downloads})")

        # имитируем загрузку
        download_time = random.uniform(1, 3)
        time.sleep(download_time)

        with active_downloads_lock:
            active_downloads -= 1
            print(f"✅ Завершена загрузка: {filename} ({download_time:.1f} сек). Осталось активных: {active_downloads}")

print("🚀 Начинаем параллельную загрузку (макс 3 одновременно)...")
start_time = time.time()

threads = []
for filename, size in files:
    t = threading.Thread(target=download_file, args=(filename, size))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total_time = time.time() - start_time
print(f"\n⏱️ Все файлы загружены за {total_time:.1f} секунд")
