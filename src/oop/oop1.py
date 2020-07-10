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

# Parent class
class Vehicle:
    pass

# Child class with Vehicle as parent
class FlightVehicle(Vehicle):
    pass

# Grandchild class with FlightVehicle as parent and Vehicle as grandparent 
class Starship(FlightVehicle):
    pass

# Grandchild class with FlightVehicle as parent and Vehicle as Grandparent
class Airplane(FlightVehicle):
    pass

# Child class with Vehicle as parent
class GroundVehicle(Vehicle):
    pass

# Grandchild class with GroundVehicle as parent and Vehicle as Grandparent
class Car(GroundVehicle):
    pass

# Grandchild class with GroundVehicle as parent and Vehicle as Grandparent
class Motorcycle(GroundVehicle):
    pass
