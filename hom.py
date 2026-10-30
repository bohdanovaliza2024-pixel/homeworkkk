class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100

    def work(self):
        self.money += 50

    def chill(self):
        self.money -= 30


liza = Student("Лиза")
liza.work()
liza.chill()
