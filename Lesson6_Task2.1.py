class Road:

    # удельная масса 1кв.м. дорожного полотна толщиной 1 см (тонн)
    _surface_spec_mass: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):

        self._length = float(length)
        self._width = float(width)

    def get_surface_mass(self, thickness: float) -> [float, None]:

        try:
            return (self._length * self._width
                    * thickness * self._surface_spec_mass)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(5000, 10)
        print(f'Масса дорожного покрытия составит: {road.get_surface_mass(20)} тонн')
    except TypeError:
        print('класс Road требует 2 позиционных аргумента')
