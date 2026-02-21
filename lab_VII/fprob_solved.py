""""""
import random


def random_ball_machine(return_balls=True, **balls):
    number_of_balls = sum(balls.values())
    colors = list(balls.keys())

    def machine():
        nonlocal number_of_balls
        if number_of_balls == 0:
            raise LookupError("urna jest pusta.")
        random_index = random.randint(1, number_of_balls)
        for color in colors:
            random_index -= balls[color]
            if random_index <= 0:
                if not return_balls:
                    balls[color] -= 1
                    number_of_balls -= 1
                return color

    return machine

