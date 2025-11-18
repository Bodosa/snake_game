from turtle import Turtle
S_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # TODO: 1. create snake body (3 squares)
    def create_snake(self):
        for position in S_POSITIONS:
            self.add_segment(position)

    # TODO: 2. move snake and changing directions
    def move(self):
        # turn to the left the snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # TODO: 7. Detect collision with tail
    def add_segment(self, position):
        new_s = Turtle("square")
        new_s.color("white")
        new_s.penup()
        new_s.goto(position)
        self.segments.append(new_s)

    def extend(self):
        self.add_segment(self.segments[-1].position())  # add in the end of the list
