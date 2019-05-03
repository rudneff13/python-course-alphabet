"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""

import constants as c
import uuid
from functools import reduce

class Cesar:
    def __init__(self, name, garages=0, register_id=hex):
        self.name = str(name)
        self.garages = garages
        self.register_id = uuid.uuid4()

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return f"Cesar attributes are: '{vars(self)}'"

    def hit_hat(self):
        return sum([sum([Car.price for Car in Garage.cars]) for Garage in self.garages])

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum([len([car for car in Garage.cars]) for Garage in self.garages])

    def add_car(self, new_car, Garage):
        if Garage in self.garages:
            if Garage.free_places() > 0:
               Garage.cars.append(new_car)
            else:
                # max_free_garage = [Garage for Garage in self.garages
                #         if Garage.free_places() == max(Garage.free_places() for Garage in self.garages)][0]
                #
                # return max_free_garage.cars.append(new_car)

                max_free_garage = reduce((lambda x, y: x if x.free_places() > y.free_places() else y), self.garages)
                if max_free_garage.free_places() > 0:
                    return max_free_garage.cars.append(new_car)
                else:
                    print("You don't have enough free space for your car!")
        else:
            print("It's not your garage!")

    def net_worth(self):
        # summa = 0
        # for Garage in self.garages:
        #     for Car in Garage.cars:
        #         summa += Car.price
        # return summa

        return sum([sum([Cars.price for Cars in Garage.cars]) for Garage in self.garages])

    def __gt__(self, other):
        return self.net_worth() > other.net_worth()

    def __lt__(self, other):
        return self.net_worth() < other.net_worth()

    def __ge__(self, other):
        return self.net_worth() >= other.net_worth()

    def __le__(self, other):
        return self.net_worth() <= other.net_worth()

    def __eq__(self, other):
        return self.net_worth() == other.net_worth()

class Car:
    def __init__(self, price, type, producer, mileage, number=hex):
        if type in c.CARS_TYPES and producer in c.CARS_PRODUCER:
            self.price = float(price)
            self.type = type
            self.producer = producer
            self.number = uuid.uuid4()
            self.mileage = float(mileage)
        else:
            print('Unknown car type or producer')

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return f"Car attributes are: '{vars(self)}'"

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def __eq__(self, other):
        return self.price == other.price

    def change_number(self, new_number):
        try:
            uuid.UUID(new_number, version=4)
            self.number = new_number
        except ValueError or AttributeError or TypeError:
            print("It's not UUID number!")

class Garage:

    def __init__(self, town, cars, places, owner=None):
        if town in c.TOWNS:
            self.town = town
            self.cars = cars
            self.places = int(places)
            self.owner = owner
        else:
            print('Unknown town name')

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return f"Garage attributes are: '{vars(self)}'"

    def add_car(self, new_car):
        free_places = self.places - len(self.cars)
        if free_places > 0:
            free_places -= 1
            self.cars.append(new_car)
            # print(free_places)
        else:
            print('Garage is full!')

    def remove_car(self, new_car):
        if new_car in self.cars:
            free_places = self.places - len(self.cars)
            if self.places - len(self.cars) < 0:
                print('How you even fit there so many cars!?')
            else:
                self.cars.remove(new_car)
                free_places += 1
            # print(free_places)
        else:
            print('No such car in garage')

    def hit_hat(self):
        return sum([Car.price for Car in self.cars])

    def free_places(self):
        return self.places - len(self.cars)

if __name__ == "__main__":

    car1 = Car(1001, "Diesel", "BMW",  1123)
    car2 = Car(2000, "Crossover", "BENTLEY", 5422)
    Garage1 = Garage('Kiev', [car1, car2], 2, "Lolka_owner")
    Garage2 = Garage('Prague', [car2], 12, "Lolka_owner")
    Garage3 = Garage('Prague', [car2, car1], 10, "Lolka_owner")
    Cesar1 = Cesar("Crappy", [Garage1, Garage2, Garage3])
    Cesar2 = Cesar("Another guy", [Garage1])

    print(car1 > car2)
    print(car1)
    print(car1.number)
    car1.change_number('c857fd34-b3e8-476a-833a-e38e1f928f6e')   #for example
    print(car1.number)

    print(Garage3.cars)
    Garage3.add_car(car1)
    print(Garage3.cars)
    Garage3.remove_car(car1)
    print(Garage3.cars)
    print(Garage3.hit_hat())

    print(Cesar1.hit_hat())
    print(Cesar1.garages_count())
    print(Cesar1.cars_count())

    print(Garage3.cars)
    print(Garage2.cars)
    print(Garage1.cars)
    Cesar1.add_car(car1, Garage1)
    print(Garage3.cars)
    print(Garage2.cars)                             # you can see by amount of cars. In result Garage2 got extra car
    print(Garage1.cars)                             # so each garage now includes 2 cars

    Cesar2.add_car(car1, Garage1)
    Cesar2.add_car(car1, Garage2)

    print(Cesar1 >= Cesar2)
