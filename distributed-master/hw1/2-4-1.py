import threading
import time
import random
import sys

def download_file(name, size):
    """Симуляция загрузки файла по частям с прогресс-баром"""
    downloaded = 0
    while downloaded < size:
        # качаем случайный кусок
        chunk = random.randint(1, 10)
        downloaded += chunk
        if downloaded > size:
            downloaded = size

        progress = int((downloaded / size) * 20)  # 20 символов ширина
        bar = "█" * progress + "-" * (20 - progress)
        sys.stdout.write(f"\r📥 {name}: |{bar}| {downloaded}/{size} MB")
        sys.stdout.flush()
        time.sleep(0.2)

    print(f"\n✅ {name} загрузка завершена!")

# список файлов
files = [
    ("Файл-A", 50),
    ("Файл-B", 70),
    ("Файл-C", 40),
]

threads = []
for name, size in files:
    t = threading.Thread(target=download_file, args=(name, size))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n🎉 Все файлы загружены!")
