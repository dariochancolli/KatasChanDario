import argparse

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    print(f"Total water left after {days_left} days is: {total_water_left} liters")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--astronauts', type=int, default=5)
    parser.add_argument('--water-left', type=int, default=100)
    parser.add_argument('--days-left', type=int, default=2)
    args = parser.parse_args()


    water_left(args.astronauts, args.water_left, args.days_left)