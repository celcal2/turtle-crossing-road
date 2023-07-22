from turtle import Turtle
import random
COLORS = ["black", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.new_car_creator()


    def new_car_creator(self):
        random_change = random.randint(1,6)
        if random_change == 1:
            new_car = Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.forward(MOVE_INCREMENT)
            y_positions = random.randint(-250, 251)
            new_car.goto(250, y_positions)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT




