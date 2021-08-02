"""
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""


def make_car(manufacturer, model, **features):
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for k, v in features.items():
        car[k] = v
    return car


car_0 = make_car('subaru', 'outback', color="blue", tow_package=True)
car_1 = make_car('logan', 'lodgy', color="white", engine="1.5 L I4 dCi")
car_2 = make_car('audi', 'a4 sport', color="black", body_style="4-door saloon")
car_3 = make_car('opel', 'astra')

cars = [car_0, car_1, car_2, car_3]

for car in cars:
    print(car)
