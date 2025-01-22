# Defines bass class Shape, and area; and derived classes Rectangle and Circle, wach overriding the area {} method to calculate respective areas

import math

class Shape:
    def area(self):
        """
        Base method to calculate the area of a shape.
        This method is intended to be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Derived class for a Rectangle.
        :param length: Length of the rectangle (float or int)
        :param width: Width of the rectangle (float or int)
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the area of a rectangle.
        :return: Area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Derived class for a Circle.
        :param radius: Radius of the circle (float or int)
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the area of a circle.
        :return: Area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)
