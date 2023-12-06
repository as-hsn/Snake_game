from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake :
    def __init__(self):
        self.snakes = []
        self.create_snake ()
        self.head = self.snakes[0]

    def create_snake(self) :
        for snake_pos in START_POSITIONS :
            self.add_snake(snake_pos)

    def add_snake(self, snake_pos):
        snake = Turtle ("square")
        snake.color ("white")
        snake.penup ()
        snake.goto (snake_pos)
        self.snakes.append (snake)

    def update_snake(self) :
       self.add_snake(self.snakes[-1].position())
    def move(self) :
        # Move the snake
        for segment_num in range ( len ( self.snakes ) - 1, 0, -1 ) :
            new_x = self.snakes[segment_num - 1].xcor ( )
            new_y = self.snakes[segment_num - 1].ycor ( )
            self.snakes[segment_num].goto (new_x, new_y )

        self.head.forward ( MOVE_DISTANCE )

    def snake_refresh(self):
        for seg in self.snakes:
            seg.hideturtle()
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]



    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
