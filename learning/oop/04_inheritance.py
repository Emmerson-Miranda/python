import time
from datetime import datetime


class Vehicle:

    def __init__(self, registration_number):
        print(f"New instance Vehicle ({self.__class__.__name__})")
        self.__created_at = datetime.now()
        self.registration_number = registration_number

    @property
    def created_at(self):
        return self.__created_at.strftime("%d/%m/%Y %H:%M:%S")

    def start(self):
        print(f"Starting Vehicle created at {self.created_at}")

    def __str__(self):
        return f"Class {self.__class__.__name__} with RegNº {self.registration_number} created at {self.created_at}"


class Terrain(Vehicle):

    def __init__(self, registration_number, wheels):
        print(f"New instance Terrain ({self.__class__.__name__})")
        Vehicle.__init__(self, registration_number)
        self.wheels = wheels

    def start(self):
        print(f"Starting Terrain created at {self.created_at}")

    def __str__(self):
        return f"Class {self.__class__.__name__} with RegNº {self.registration_number} created at {self.created_at} Nºwheels {self.wheels}"


class Aquatic(Vehicle):

    def __init__(self, registration_number, propeller):
        print(f"New instance Aquatic ({self.__class__.__name__})")
        Vehicle.__init__(self, registration_number)
        self.propeller = propeller

    def start(self):
        print(f"Starting Aquatic created at {self.created_at}")

    def __str__(self):
        return f"Class {self.__class__.__name__} with RegNº {self.registration_number} created at {self.created_at} Nºpropeller {self.propeller}"


class Car(Terrain):

    def __init__(self, registration_number, wheels):
        print(f"New instance Car ({self.__class__.__name__})")
        super().__init__(registration_number, wheels)

    def start(self):
        print(f"Starting Car created at {self.created_at}")


class Bus(Terrain):

    def __init__(self, registration_number, wheels):
        print(f"New instance Bus ({self.__class__.__name__})")
        super().__init__(registration_number, wheels)


class Boat(Aquatic):

    def __init__(self, registration_number, propeller):
        print(f"New instance Boat ({self.__class__.__name__})")
        Aquatic.__init__(self, registration_number, propeller)

    def start(self):
        print(f"Starting Boat created at {self.created_at}")


class Amphibious(Car, Boat):

    def __init__(self, registration_number, wheels, propeller):
        print(f"New instance Amphibious ({self.__class__.__name__})")
        Car.__init__(self, registration_number, wheels)
        Boat.__init__(self, registration_number, propeller)


class Amphibious2(Boat, Car):

    def __init__(self, registration_number, wheels, propeller):
        print(f"New instance Amphibious2 ({self.__class__.__name__})")
        Boat.__init__(self, registration_number, propeller)
        Car.__init__(self, registration_number, wheels)


if __name__ == '__main__':
    line = "-" * 80

    print(line, "| 01 ", line, sep="\n")
    vehicle = Vehicle("abc123A")
    vehicle.start()
    print(vehicle, "\n\n")

    print(line, "| 02 ", line, sep="\n")
    terrain = Terrain("abc123B", 4)
    terrain.start()
    print(terrain, "\n\n")

    print(line, "| 03 ", line, sep="\n")
    aquatic = Aquatic("abc123C", 1)
    aquatic.start()
    print(aquatic, "\n\n")

    print(line, "| 04 ", line, sep="\n")
    car = Car("abc123D", 4)
    car.start()
    print(car, "\n\n")

    print(line, "| 05 ", line, sep="\n")
    boat = Boat("abc123E", 1)
    boat.start()
    print(boat, "\n\n")

    print(line, "| 06 Multi inheritance - Car precedence", line, sep="\n")
    amphibious = Amphibious("abc123F", 4, 1)
    amphibious.start()
    print(amphibious, "\n\n")

    print(line, "| 07 Multi inheritance - Boat precedence", line, sep="\n")
    amphibious2 = Amphibious2("abc123G", 4, 1)
    amphibious2.start()
    print(amphibious2, "\n\n")

    print(line, "| 08 __bases__, type and isinstance", line, sep="\n")
    print("Class", type(vehicle).__name__, " base ", Vehicle.__bases__)
    print("Class", type(terrain).__name__, " base ", Terrain.__bases__)
    print("Class", type(car).__name__,     " base ", Car.__bases__)
    print("Class", type(aquatic).__name__, " base ", Aquatic.__bases__)
    print("Class", type(boat).__name__,    " base ", Boat.__bases__)
    print("Class", type(amphibious).__name__,  " base ", Amphibious.__bases__)
    print("Class", type(amphibious2).__name__, " base ", Amphibious2.__bases__, "\n\n")

    print(line, "| 09 isinstance", line, sep="\n")
    print("vehicle is Vehicle", isinstance(vehicle, Vehicle))
    print("terrain is Terrain", isinstance(terrain, Terrain))
    print("terrain is Vehicle", isinstance(terrain, Vehicle))
    print("car is Car", isinstance(car, Car))
    print("car is Terrain", isinstance(car, Terrain))
    print("car is Vehicle", isinstance(car, Vehicle))
    print("car is Aquatic", isinstance(car, Aquatic))

    print("aquatic is Aquatic", isinstance(aquatic, Aquatic))
    print("aquatic is Vehicle", isinstance(aquatic, Vehicle))

    print("boat is Boat",  isinstance(boat, Boat))
    print("boat is Aquatic",  isinstance(boat, Aquatic))
    print("boat is Vehicle",  isinstance(boat, Vehicle))
    print("boat is Terrain",  isinstance(boat, Terrain))

    print("amphibious is Amphibious", isinstance(amphibious, Amphibious))
    print("amphibious is Car", isinstance(amphibious, Car))
    print("amphibious is Bus", isinstance(amphibious, Bus))
    print("amphibious is Boat", isinstance(amphibious, Boat))
    print("amphibious is Boat", isinstance(amphibious, Aquatic))
    print("amphibious is Terrain", isinstance(amphibious, Terrain))
    print("amphibious is Car and Boat", isinstance(amphibious, (Car, Boat)))
    print("amphibious is Boat and Car", isinstance(amphibious, (Boat, Car)))
