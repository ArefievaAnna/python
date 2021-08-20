"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""

from time import sleep
from datetime import datetime as dt


class TrafficLight:
    # Класс светофора, реализующий свое переключение при запуске running
    _states = {'red': 7, 'yellow': 2, 'green': 10}
    __color = ''

    def running(self):
        # Метод запуска светофора
        for color, sw_time in self._states.items():
            self.__color = color
            start_state_time = dt.now()

            print(f"TrafficLight switched to state '{self.__color}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"TrafficLight leave state '{self.__color}' after" 
                  f"{(dt.now() - start_state_time).seconds} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()

