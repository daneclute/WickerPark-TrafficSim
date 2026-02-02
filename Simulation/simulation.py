import simpy
import random
import pandas as pd
from load_data import get_data

class Street:
    def __init__(self, segment_id, street, direction, from_street, to_street, length, curr_speed, env):
        self.segment_id = segment_id
        self.street = street
        self.direction = direction
        self.from_street = from_street
        self.to_street = to_street
        self.length = float(length)
        self.curr_speed = int(curr_speed)
        self.env = env
        self.lane_q = []
    
    def __str__(self):
        return f'{self.direction}'

    def add_car(self, car):
        self.lane_q.append(car)
        self.env.process(self.move_cars(car))
    
    def move_cars(self, car):
        travel_time = (self.length / self.curr_speed)
        yield self.env.timeout(travel_time)
        print(f'{car.name} arrived at {self.to_street} at time {self.env.now:.2f} minutes')
            
        self.lane_q.remove(car)


class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'
    
    
def generate_cars(env, car, street, delay_func):
    yield env.timeout(delay_func())
    print(f'{car} starting at {street.from_street} going {street.direction} at {street.curr_speed}mph')
    street.add_car(car)