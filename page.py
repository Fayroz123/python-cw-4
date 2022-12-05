def my_name(name):
   print(f"My name is {name}")

my_name("Fayroz")


def my_meal(food,drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal("fish","coffee")


def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else: False
