class NullCar(object):

    def __init__(self, car_name):
        self.car_name = car_name
    def start(self):
        print(f"Unknown car {self.car_name}")

    def stop(self):
        pass
