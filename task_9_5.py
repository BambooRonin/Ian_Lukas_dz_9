class Stationery:
    def __init__(self, title='Инструменты для рисования'):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать')


class Pen(Stationery):
    def draw(self):
        print(f'Начинаем рисовать. Инструмент: {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Начинаем рисовать. Инструмент: {self.title}')


class Marker(Stationery):
    def draw(self):
        print(f'Начинаем рисовать. Инструмент: {self.title}')


a = Stationery()
a.draw()
pen = Pen('Bic')
pen.draw()
pencil = Pencil('Centrum')
pencil.draw()
marker = Marker('Copic')
marker.draw()
