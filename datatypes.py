# Description: Main file for the project
def datatypes():
    first_name = "Jaya"
    food = "Pizza"

    print(first_name + " loves to eat " + food)
    print(f"I am {first_name} and I love to eat {food}")
    print("I am {} and I love to eat {}".format(first_name, food))

    # strings
    first_name = "Jaya"
    food = "pizza"
    email = "jaya!@fake.com"

    # Integer
    age = 30

    # float
    price = 10.99
    gpa = 3.2

    # boolean
    is_student = True
    is_teacher = False

    print(f"Are you a student?: {is_student}")
    print(f"your gps is: {gpa}")
    print(f"I am {first_name} and I am {age} years old")
    print("I am {} and I am {} years old".format(first_name, age))


    if is_student:
        print("Yes")
    else:
        print("No")

def typecasting():
    name = "jaya"
    age = 30
    gpa = 3.2
    is_student = False
    print(type(name))

    gpa = int(gpa)
    print(type(gpa))

    age = float(age)
    print(type(age))

    age = str(age)
    print(type(age))

    age += "1"
    print(age)

    name = bool(name)
    print(name)
    name_empty = bool("")
    print(name_empty)


if __name__ == "__main__":
    datatypes()
    print("executed datatypes()")

    typecasting()




