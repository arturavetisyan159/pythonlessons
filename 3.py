# Задание 3- создание класса Robot

class Robot:
    count = 0

    def __init__(self, name):
        print("Инициализация робота:", name)
        self.name = name
        print("Приветствую, меня зовут:", self.name)
        Robot.count += 1
        print("Численность роботов:", Robot.count)

    def work(self):
        print("\n\nЗдесь роботы делают какуюто работу\n\n")
    
    def __del__(self):
        print("Роботы закончили свою работу!\n...выключение... ")
        print(self.name, "выключается")
        Robot.count -= 1
        print("работающих роботов осталось", Robot.count)
        if Robot.count == 0:
            print(self.name, "был последним")

first = Robot('r2-d2')
second = Robot("robox")
first.work()

