import threading
import time
import random

teams = {
    "красные": ["🚗 Красная-1", "🚗 Красная-2"],
    "синие": ["🚙 Синяя-1", "🚙 Синяя-2"]
}
points_system = [10, 8, 6, 4, 2]

finish_order = []
finish_lock = threading.Lock()
team_scores = {"красные": 0, "синие": 0}

class Car(threading.Thread):
    def __init__(self, name, distance, team):
        super().__init__()
        self.name = name
        self.distance = distance
        self.position = 0
        self.team = team

    def run(self):
        while self.position < self.distance:
            step = random.randint(1, 4)
            self.position += step
            if self.position > self.distance:
                self.position = self.distance
            time.sleep(0.2)
        print(f"🏁 {self.name} финишировал!")
        with finish_lock:
            finish_order.append((self.name, self.team))


# Создаём машинки
race_distance = 50
cars = []
for team, names in teams.items():
    for name in names:
        cars.append(Car(name, race_distance, team))

# Стартуем
for car in cars: car.start()
for car in cars: car.join()

# Начисляем очки
for place, (car_name, team) in enumerate(finish_order, start=1):
    if place <= len(points_system):
        points = points_system[place - 1]
    else:
        points = 0
    team_scores[team] += points
    print(f"{place}-е место: {car_name} ({team}) +{points} очков")

# Итог
print("\n📊 Результаты по командам:")
for team, score in team_scores.items():
    print(f"Команда {team}: {score} очков")

winner = max(team_scores, key=team_scores.get)
print(f"\n🏆 Победитель: команда {winner}!")
