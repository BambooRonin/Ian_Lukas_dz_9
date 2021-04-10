class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self):
        return self._length * self._width * 25 * 5


a = Road(6, 6000)
print(str(a.asphalt_mass()) + ' тонн')
