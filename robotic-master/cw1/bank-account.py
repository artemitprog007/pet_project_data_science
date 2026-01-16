class BankAccount:
    bank_name = "Python Bank"  # классовый атрибут
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = id(self)  # уникальный номер счета
    
    def deposit(self, amount):
        """Положить деньги на счет"""
        if amount > 0:
            self.balance += amount
            return f"Внесено {amount}. Баланс: {self.balance}"
        else:
            return "Сумма должна быть положительной"
    
    def withdraw(self, amount):
        """Снять деньги со счета"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Снято {amount}. Баланс: {self.balance}"
        else:
            return "Недостаточно средств или неверная сумма"
    
    def get_balance(self):
        """Проверить баланс"""
        return f"Баланс счета: {self.balance}"

# Использование
account1 = BankAccount("Иван Иванов", 1000)
account2 = BankAccount("Петр Петров")

print(account1.deposit(500))      # Внесено 500. Баланс: 1500
print(account1.withdraw(200))     # Снято 200. Баланс: 1300
print(account2.deposit(100))      # Внесено 100. Баланс: 100

print(f"Банк: {BankAccount.bank_name}")