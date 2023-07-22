import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Celiny gra w samochodziki")
screen.setup(width=600, height=600)
screen.tracer(0)

me = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(me.move_up, "Up")
screen.onkey(me.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car_creator()
    car.move_car()

    # detect collision with a car
    for car in car.all_cars:
        if car.distance(me) < 20:
            game_is_on = False
            score.game_over()

    # detect crossing the screen
    if me.cross_the_road():
        me.go_to_start()
        car.level_up()
        score.increase_level()



screen.exitonclick()

