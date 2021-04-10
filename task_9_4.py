class Car:
    def __init__(self, name, colour, speed, police=False):
        self.name = name
        self.colour = colour
        self.speed = speed
        self.police = police
        print(f'Новая машина: {self.name}, цвет {self.colour}, полицейская {police}')

    def go(self):
        print(f'{self.name}: Машина тронулась')

    def stop(self):
        print(f'{self.name}: Машина остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        return f'{self.name}: скорость: {self.speed}'


class Towncar(Car):
    def show_speed(self):
        return f'{self.name}: скорость: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f'{self.name}: скорость: {self.speed}'

class Workingcar(Car):
    def show_speed(self):
        return f'{self.name}: скорость: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f'{self.name}: скорость: {self.speed}'

class Sportscar(Car):
    def show_speed(self):
        return f'{self.name}: скорость: {self.speed}. Превышение скорости!' \
            if self.speed > 80 else f'{self.name}: скорость: {self.speed}'

class Policecar(Car):
    def __init__(self, name, colour, speed, police = True):
        super().__init__(name, colour, speed, police)


towncar = Towncar("Шевроле", "серебристая", 57)
towncar.go()
towncar.turn(1)
towncar.turn(0)
print(towncar.show_speed())
towncar.stop()
print()

policecar = Policecar("Тойота", "синяя", 78)
policecar.go()
policecar.turn(1)
policecar.turn(0)
print(policecar.show_speed())
policecar.stop()
print()

workingcar = Workingcar("КАМАЗ", "оранжевый", 43)
workingcar.go()
workingcar.turn(1)
workingcar.turn(0)
print(workingcar.show_speed())
workingcar.stop()
print()

sportscar = Sportscar("Бугатти", "красный", 120)
sportscar.go()
sportscar.turn(1)
sportscar.turn(0)
print(sportscar.show_speed())
sportscar.stop()
