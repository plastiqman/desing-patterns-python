
from auto_factory import AutosFactory

factory = AutosFactory()

for car_name in 'ChevyVolt', 'FordFusion', 'JeepSahara', 'Tesla Roadster':
    car = factory.create_instance(car_name)
    car.start()
    car.stop()