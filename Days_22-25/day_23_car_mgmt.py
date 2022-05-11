from turtle import Turtle
import random

COLORS = ["red", "orange", "gold", "green", "blue", "purple"]
STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        self.speed = STARTING_MOVE_DIST

    def move_car(self):
        self.backward(STARTING_MOVE_DIST)


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.generate_cars()

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Car()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move_car()

    def increase_speed(self):
        for car in self.cars:
            car.speed += MOVE_INCREMENT

