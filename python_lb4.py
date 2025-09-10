import time

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Внесення грошей на рахунок."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} гривень внесено на рахунок.")
        else:
            print("Сума внесення повинна бути більшою за 0.")

    def withdraw(self, amount):
        """Зняття грошей з рахунку."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} гривень знято з рахунку.")
        else:
            print("Недостатньо коштів або невірна сума для зняття.")

    def check_balance(self):
        """Перевірка поточного балансу рахунку."""
        print(f"Поточний баланс рахунку {self.owner}: {self.balance} гривень.")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Обчислення відсотків на баланс."""
        interest = self.balance * self.interest_rate
        print(f"Відсотки на поточний баланс ({self.balance} гривень): {interest} гривень.")
        return interest

    def add_interest(self):
        """Додавання відсотків до балансу."""
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Відсотки додано до балансу. Новий баланс: {self.balance} гривень.")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=1000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def process_check(self, check_amount):
        """Обробка чеку."""
        if check_amount <= self.balance + self.overdraft_limit:
            self.balance -= check_amount
            print(f"Чек на суму {check_amount} гривень був оброблений. Новий баланс: {self.balance} гривень.")
        else:
            print(f"Недостатньо коштів на рахунку для обробки чеку на суму {check_amount} гривень.")

# акаунти
bank_account = BankAccount("Іван", 500)

savings_account = SavingsAccount("Марія", 1000, 0.05)

checking_account = CheckingAccount("Андрій", 500, 1000)

# інтерфейс
def interact_with_account():
    print("Виберіть рахунок:")
    account_type = input("1 - Банківський рахунок, 2 - Ощадний рахунок, 3 - Розрахунковий рахунок, 4 - Вихід: ")

    if account_type == "1":
        interact_BankAccount()
        return

    elif account_type == "2":
        interact_SavingsAccount()
        return
    
    elif account_type == "3":
        interact_CheckingAccount()
        return
    
    elif account_type == "4":
        return
    
    else:
        print("Невірний вибір, спробуйте ще раз")
        interact_with_account()
        return
    
def interact_BankAccount():
    print("\nВиберіть операцію:")
    print("1. Внести гроші")
    print("2. Зняти гроші")
    print("3. Перевірити баланс")
    print("4. Змінити рахунок")
    action_type = input()
    if action_type == "1":
        bank_account.deposit(int(input("Внесіть гроші: ")))
        interact_BankAccount()
        return

    elif action_type == "2":
        bank_account.withdraw(int(input("Зняти гроші: ")))
        interact_BankAccount()
        return
    
    elif action_type == "3":
        bank_account.check_balance()
        time.sleep(1)
        interact_BankAccount()
        return
    
    elif action_type == "4":
        interact_with_account()
        return
    
    else:
        print("Невірний вибір, спробуйте ще раз")
        interact_BankAccount()
        return

def interact_SavingsAccount():
    print("\nВиберіть операцію:")
    print("1. Обчислити відсотки")
    print("2. Додати відсотки")
    print("3. Змінити рахунок")
    action_type = input()
    if action_type == "1":
        savings_account.check_balance()
        time.sleep(1)
        interact_SavingsAccount()
        return

    elif action_type == "2":
        savings_account.add_interest()
        time.sleep(1)
        interact_SavingsAccount()
        return
    
    elif action_type == "3":
        interact_with_account()
        return
    
    else:
        print("Невірний вибір, спробуйте ще раз")
        interact_SavingsAccount()
        return

def interact_CheckingAccount():
    print("\nВиберіть операцію:")
    print("1. Обробити чек")
    print("2. Перевірити баланс")
    print("3. Змінити рахунок")
    action_type = input()
    if action_type == "1":
        checking_account.process_check(int(input("Сума чеку: ")))
        interact_CheckingAccount()
        return
    
    elif action_type == "2":
        checking_account.check_balance()
        time.sleep(1)
        interact_CheckingAccount()
        return
    
    elif action_type == "3":
        interact_with_account()
        return
    
    else:
        print("Невірний вибір, спробуйте ще раз")
        interact_CheckingAccount()
        return
    
interact_with_account()