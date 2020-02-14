# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    pass


# Base ==> Vehicle


class GroundVehicle(Vehicle):
    pass


# Base ==> GroundVehicle


class Car(GroundVehicle):
    pass


# Base ==> GroundVehicle


class Motorcycle(GroundVehicle):
    pass


# Base ==> Vehicle


class FlightVehicle(Vehicle):
    pass


# Base ==> FlightVehicle


class Airplane(FlightVehicle):
    pass


# Base ==> FlightVehicle


class Starship(FlightVehicle):
    pass
