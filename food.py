from turtle import Turtle
import random

class Food (Turtle) :
    def __init__(self) :
        super ().__init__ ()
        self.shape ("circle")
        self.penup ()
        self.shapesize (0.6,
                        0.6)
        self.color ("blue")
        self.refresh ()

    def refresh(self) :
        x_exis = random.randint (-280,
                                 280)
        y_exis = random.randint (-280,
                                 250)
        self.goto (x_exis,
                   y_exis)
