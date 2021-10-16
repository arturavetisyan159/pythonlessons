# Класс Time

from datetime import datetime

class Time:
    timezone = 0

    def __init__(self, moment):
        if Time.check_time(moment):
            hour = int(moment.split(':')[0])
            minute = int(moment.split(':')[1])
            second = int(moment.split(':')[2])
            self.hour = hour
            self.minute = minute
            self.second = second
            if Time.timezone >= 0:
                print(f"Отметка времени: {self.hour}:{self.minute}:{self.second} UTC+{Time.timezone}")
                print('-'*50)
            else:
                print(f"Отметка времени: {self.hour}:{self.minute}:{self.second} UTC{Time.timezone}")
                print('-'*50)
        else:
            print("Неверные данные.")
            print("--------------------")

    def __del__(self):
        print('-'*50)
        print(f"Отметка времени удалена: ", end=' ')
        self.print_time()

    @classmethod
    def timezone_change(cls, zone):
        if isinstance(zone, int) and zone >= -12 and zone <= 14:
            cls.timezone = zone
            if cls.timezone >= 0:
                print(f"UTC+{cls.timezone}")
                print("-"*50)
            else:
                print(f"UTC{cls.timezone}")
                print("-"*50)
        else:
            print("Неверно введен часовой пояс!")

    @staticmethod
    def check_time(moment):
        if moment.count(":") != 2:
            return False
        else:
            moment = moment.split(':')
            hr = int(moment[0])
            min = int(moment[1])
            sec = int(moment[2])
            if hr >= 24 or hr < 0 or min > 59 or min < 0 or sec > 59 or sec < 0:
                return False
            return True

    @staticmethod
    def sec_to_moment(seconds):
        hour = seconds // 3600
        minute = (seconds - 3600 * hour) // 60
        second = seconds - (3600 * hour + minute * 60)
        res = f"{hour}:{minute}:{second}"
        return res

    @staticmethod
    def moment_to_sec(moment):
        datetimeformat = '%H:%M:%S'
        moment_to_sec = datetime.strptime(moment, datetimeformat)
        return moment_to_sec

    def print_time(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

    def time_diff(self, moment):
        str_default = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)
        if not Time.check_time(moment):
            return "Неправильно введенно время!"
        diff = abs((Time.moment_to_sec(str_default) - Time.moment_to_sec(moment)).total_seconds())
        res = f"Разница между {str_default} и {moment} составила {diff} секунд!"
        print(res)

    def add_sec():
        pass