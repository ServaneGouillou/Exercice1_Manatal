#ex 1 : 10 minutes

import numpy as np

class Circle:
    """
    The Class Circle is used to construct a circle.

    Parameters
    -----------
    radius : float : radius of the circle
    -----------

    Example
    -----------
    circle_1 = Circle (radius = 3.3 )
    """

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """
        Calculate the area of the circle
        """
        area = np.pi * (self.radius **2)
        return area

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the circle
        """
        perimeter = 2 * np.pi * self.radius
        return perimeter


