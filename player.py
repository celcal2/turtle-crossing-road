from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color('red')
        self.setheading(90)
        self.y_start = -280
        # self.move()
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(-MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def cross_the_road(self):
       if self.ycor() > FINISH_LINE_Y:
           return True
       else: return False


