#!/usr/bin/python3
"""Module for Base class."""
import json
import os
import csv
import turtle

class Base:
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # ... rest of your Base class code ...

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares."""
        window = turtle.Screen()
        window.bgcolor("white")
        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.right(90)
                t.forward(rect.height)
                t.right(90)

        t.color("blue")

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.right(90)

        window.exitonclick()
