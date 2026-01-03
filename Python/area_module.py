import math

def circle(radius:float):
    if radius < 0:
        raise ValueError("Radius can't be less than 0")
    return (math.pi * radius * radius)

def triangle(base:float, height:float):
    if base < 0 or height < 0:
        raise ValueError("Base and height can't be less than 0")
    return (0.5 * base * height)

def square(side:float):
    if side < 0:
        raise ValueError("Side can't be less than 0")
    return (side * side)

def rectangle(length:float, width:float):
    if length < 0 or width < 0:
        raise ValueError("Length and width can't be less than 0")
    return (length * width)