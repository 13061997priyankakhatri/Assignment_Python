"""
Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example usage:
# Create an instance of Rectangle
rectangle = Rectangle(6, 13)

# Compute and print the area of the rectangle
area = rectangle.compute_area()
print(f"The area of the rectangle is: {area}")
