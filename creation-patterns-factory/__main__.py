from chevy_volt import ChevyVolt
from ford_fusion import FordFusion
from jeep_sahara import JeepSahara
from null_car import NullCar


def get_car(brand: str):
    if brand == 'Chevy':
        return ChevyVolt()
    if brand == 'Ford':
        return FordFusion()
    if brand == 'Jeep':
        return JeepSahara()

    return NullCar(car)


for car_name in 'Chevy', 'Ford', 'Jeep', 'Tesla':
    car = get_car(car_name)
    car.start()
    car.stop()

