import simpy
import random
import os
import pandas as pd
from simulation import Street, Car, generate_cars
from load_data import get_data
from dotenv import load_dotenv



def main():
    data = get_data()

    if not data:
        print('Could not fetch data')

    segment208 = None
    for segmentid in data:
        if segmentid.get('segmentid') == '208':
            segment208 = segmentid
            break

    env = simpy.Environment()
    delay_func = lambda: random.triangular(0,10,2)

    north_ave = Street(
        segment_id=segment208['segmentid'],
        street=segment208['street'],
        direction=segment208['_direction'],
        from_street=segment208['_fromst'],
        to_street=segment208['_tost'],
        length=segment208['_length'],
        curr_speed=segment208['_traffic'],
        env=env
    )


    print(f"\nSimulating: {north_ave}")
    print(f"Length: {north_ave.length} miles, Speed: {north_ave.curr_speed} mph")
    print("=" * 60)
    
    for i in range(10):
        car = Car(f'Car {i+1}')
        env.process(generate_cars(env, car, north_ave, delay_func))

    env.run(until=200)

    print("=" * 60)
    print("Simulation complete!")

if __name__ == "__main__":
    main()