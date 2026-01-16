import threading
import time
import random

obstacle_positions = [30, 60, 80]  # препятствия
boost_positions = [20, 50, 70]     # ускорения

class Car(threading.Thread):
    def __init__(self, name, distance, base_speed=1):
        super().__init__()
        self.name = name
        self.distance = distance
        self.position = 0
        self.speed = base_speed
        self.base_speed = base_speed
        self.boost_end_time = 0

    def run(self):
        while self.position < self.distance:
            # проверяем ускорение
            if self.position in boost_positions and time.time() > self.boost_end_time:
                print(f"⚡ {self.name} получил ускорение!")
                self.speed = self.base_speed * 2
                self.boost_end_time = time.time() + 2  # ускорение на 2 сек

            # проверяем окончание ускорения
            if time.time() > self.boost_end_time:
                self.speed = self.base_speed

            # проверяем препятствия
            if self.position in obstacle_positions:
                print(f"⛔ {self.name} столкнулся с препятствием!")
                time.sleep(0.5)

            # двигаемся
            step = random.randint(1, 3) * self.speed
            self.position += step
            if self.position > self.distance:
                self.position = self.distance

            print(f"{self.name} на позиции {self.position}/{self.distance} (скорость {self.speed})")
            time.sleep(0.3)

        print(f"🏁 {self.name} финишировал!")


# Запуск гонки
race_distance = 100
cars = [
    Car("🚗 Машина-1", race_distance),
    Car("🚙 Машина-2", race_distance),
    Car("🚕 Машина-3", race_distance),
]

for car in cars:
    car.start()

for car in cars:
    car.join()

print("🎉 Гонка завершена!")
