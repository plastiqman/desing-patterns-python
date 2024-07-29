from .auto import Auto


class NullCar(Auto):
    def __init__(self, car_name: str):
        self._car_name = car_name

    def start(self):
        print(f"Unknown {self._car_name}")

    def stop(self):
        pass
