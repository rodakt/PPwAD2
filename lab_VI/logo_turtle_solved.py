from math import sin, cos, radians
import csv

def create_turtle(x=0, y=0, azimuth=0, name=''):
    return {'position': [(x, y)], 'azimuth': azimuth, 'name': name}

def left(turtle, angle):
    turtle['azimuth'] += angle

def right(turtle, angle):
    turtle['azimuth'] -= angle

def forward(turtle, distance):
    azimuth = radians(turtle['azimuth'])
    x, y = turtle['position'][-1]
    x = x + distance * cos(azimuth)
    y = y + distance * sin(azimuth)
    turtle['position'].append((x, y))

def to_csv(*turtles, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y', 'name'])
        for turtle in turtles:
            for x, y in turtle['position']:
                writer.writerow([x, y, turtle['name']])

if __name__ == '__main__':

    import random

    turtles = [create_turtle(azimuth=random.choice([-45, 45]), name=f'turtle_{i}') for i in range(20)]

    for _ in range(100):
        for turtle in turtles:
            if turtle['azimuth'] == 45:
                angle = random.choice([0, 90])
            else:
                angle = random.choice([0, -90])
            right(turtle, angle)
            forward(turtle, 1)


    to_csv(*turtles, filename='/tmp/dump.csv')
