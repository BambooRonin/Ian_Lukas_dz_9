from time import sleep


class TrafficLight:
    __colour = ('Красный', 'Желтый', 'Зеленый')

    def running(self):
        print("\033[31m {}".format(TrafficLight.__colour[0]))
        sleep(7)
        print("\033[33m {}".format(TrafficLight.__colour[1]))
        sleep(2)
        print("\033[32m {}".format(TrafficLight.__colour[2]))
        sleep(5)


a = TrafficLight()
a.running()
