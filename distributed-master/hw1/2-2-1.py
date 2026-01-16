import threading
import time

class BankAccount:
    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()
        self.history = []  # история операций
        self.history_lock = threading.Lock()  # отдельный lock для истории

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                time.sleep(0.1)  # имитация задержки
                self.balance -= amount
                msg = f"Снятие {amount}. Остаток: {self.balance}"
            else:
                msg = f"❌ Недостаточно средств для снятия {amount}. Баланс: {self.balance}"

        # запись в историю
        with self.history_lock:
            self.history.append(msg)
        print(msg)

    def deposit(self, amount):
        with self.lock:
            time.sleep(0.1)  # имитация задержки
            self.balance += amount
            msg = f"Пополнение {amount}. Остаток: {self.balance}"

        # запись в историю
        with self.history_lock:
            self.history.append(msg)
        print(msg)


# Создаем счёт
account = BankAccount()

# Функции для потоков
def customer_withdraw():
    for _ in range(3):
        account.withdraw(30)

def customer_deposit():
    for _ in range(3):
        account.deposit(50)


# Создаем потоки: 2 снимают, 2 пополняют
threads = []
for i in range(2):
    t = threading.Thread(target=customer_withdraw, name=f"Снятие-{i}")
    threads.append(t)
    t.start()

for i in range(2):
    t = threading.Thread(target=customer_deposit, name=f"Пополнение-{i}")
    threads.append(t)
    t.start()

# Ждем все потоки
for t in threads:
    t.join()

print("\n📜 История операций:")
for record in account.history:
    print(record)

print(f"\n💰 Итоговый баланс: {account.balance}")
