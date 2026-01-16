import threading
import time

MAX_BALANCE = 500
COMMISSION = 1

class BankAccount:
    def __init__(self):
        self.balance = 100
        self.max_balance = MAX_BALANCE
        self.lock = threading.Lock()
        self.history = []
        self.history_lock = threading.Lock()

    def withdraw(self, amount):
        total = amount + COMMISSION
        with self.lock:
            if self.balance >= total:
                time.sleep(0.1)
                self.balance -= total
                msg = f"Снятие {amount} + комиссия {COMMISSION}. Остаток: {self.balance}"
            else:
                msg = f"❌ Недостаточно средств для снятия {amount} (нужно {total}). Баланс: {self.balance}"

        with self.history_lock:
            self.history.append(msg)
        print(msg)

    def deposit(self, amount):
        with self.lock:
            if self.balance + amount > self.max_balance:
                msg = f"❌ Пополнение {amount} отклонено: лимит {self.max_balance}, баланс: {self.balance}"
            else:
                time.sleep(0.1)
                self.balance += amount
                msg = f"Пополнение {amount}. Остаток: {self.balance}"

        with self.history_lock:
            self.history.append(msg)
        print(msg)


# Создаем счёт
account = BankAccount()

# Потоки
def withdraw_task():
    for _ in range(3):
        account.withdraw(30)

def deposit_task():
    for _ in range(3):
        account.deposit(200)

threads = []
# 2 потока на снятие
for i in range(2):
    t = threading.Thread(target=withdraw_task, name=f"Снятие-{i}")
    threads.append(t)
    t.start()

# 2 потока на пополнение
for i in range(2):
    t = threading.Thread(target=deposit_task, name=f"Пополнение-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n📜 История операций:")
for record in account.history:
    print(record)

print(f"\n💰 Итоговый баланс: {account.balance}")
