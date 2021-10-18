# Добавить геттеры и сеттеры в класс Account

class Account:
    rate_usd = 0.014
    rate_eur = 0.012
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num}, принадлежащий {self.__surname}, был октрыт")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num}, принадлежащий {self.__surname}, был закрты")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, s):
        self.__surname = s

    @property
    def percent(self):
        return self.percent

    @percent.setter
    def percent(self, p):
        self.__percent = p

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    def print_balance(self):
        print(f"Текущий баланс: {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Процент: {self.__percent : .0%}")
        print("-" * 20)

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}.")
        else:
            self.__value = self.__value - val
            print(f"{val} {Account.suffix} были успешно сняты.")
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} быди успешно добавлены.")
        self.print_balance()


acc = Account("Долгих", 12321, 0.03, 1000)
acc.print_info()
acc.num = 1984
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(3)
Account.set_eur_rate(4)
acc.convert_to_usd()
acc.convert_to_eur()
acc.surname = "Иванов"
acc.percent = 0.15
acc.value = 2000
acc.print_info()
print()
acc.add_percents()
print()
acc.withdraw_money(300)
acc.withdraw_money(3000)
print()
acc.add_money(5000)
acc.withdraw_money(3000)

