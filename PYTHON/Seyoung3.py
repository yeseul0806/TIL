def double(n):
    return n*2
print(double(1))
print(double(2))

def add(x,y):
    result = x+y
    return result
print(add(1,3))

def bmi(weight, height):
    """Calculate BMI(Body Mass Index) with weight and height.

    Parameters:
    weight: Body weight in kilograms.
    height: Body height in meters.
    """

    return weight/(height ** 2)
print(bmi(68, 1.82))

print(bmi.__doc__)
help(bmi)


def factorial(n):
    accumulator = 1
    for i in range(1, n+1):
        accumulator *= i
    return accumulator
print(factorial(5))