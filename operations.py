import math

print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(3.1))
print(math.floor(3.1))

radius = float(input('Enter the radius of the circle'))
circumference = 2 * math.pi * radius
print(f"circumference: {round(circumference, 2)}")

area = math.pi * pow(radius, 2)
print("Area is: {}".format(area))


def arithmetic_op():
    friends = 2
    friends = friends + 1
    friends += 1
    print(friends)

    friends -= 2
    friends *= 3
    friends /= 2
    print(friends)

    friends **= 2
    rem = friends % 3
    print(rem)
    print(friends)

def math():
    x = 3.14
    y = 4
    z = 5
    result = round(x)
    print(result)
    result1 = abs(x)
    result2 = pow(x, y)
    print(result2)
    print(max(x, y, z))
    print(min(x, y, z))


if __name__ == '__main__':
    # arithmetic_op()
    # math()
    pass