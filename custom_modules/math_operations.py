import math

def factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return math.factorial(n)


def compound_interest(principal, rate, time_years):

    amount = principal * (1 + rate / 100) ** time_years

    return amount


def trigonometry(angle):

    radians = math.radians(angle)

    return {
        "sin": math.sin(radians),
        "cos": math.cos(radians),
        "tan": math.tan(radians)
    }


def circle_area(radius):

    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    return math.pi * radius ** 2


def rectangle_area(length, width):

    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")

    return length * width


def triangle_area(base, height):

    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")

    return 0.5 * base * height