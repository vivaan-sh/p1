"""
Vehicle Information System

This program demonstrates the concept of inheritance.
A base class 'Vehicle' is created and a derived class 'Car'
inherits the properties of Vehicle and adds additional attributes.
"""

class Vehicle:
    """
    Base class representing a general vehicle.
    """

    def __init__(self, vehicle_id, brand, price):
        """
        Constructor to initialize vehicle attributes.

        Args:
            vehicle_id (int): Unique ID of the vehicle
            brand (str): Brand name of the vehicle
            price (float): Price of the vehicle
        """
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.price = price

    def display_vehicle(self):
        """
        Displays the basic vehicle details.
        """
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Price:", self.price)


class Car(Vehicle):
    """
    Derived class representing a car.
    Inherits attributes from Vehicle and adds car-specific details.
    """

    def __init__(self, vehicle_id, brand, price, num_doors, fuel_type):
        """
        Constructor to initialize car attributes.

        Args:
            num_doors (int): Number of doors in the car
            fuel_type (str): Type of fuel used (Petrol/Diesel/Electric)
        """
        super().__init__(vehicle_id, brand, price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_car_details(self):
        """
        Displays complete car details including vehicle information.
        """
        self.display_vehicle()
        print("Number of Doors:", self.num_doors)
        print("Fuel Type:", self.fuel_type)
        print("---------------------------")


# Creating car objects
car1 = Car(101, "Toyota", 1500000, 4, "Petrol")
car2 = Car(102, "Tesla", 4500000, 4, "Electric")

# Display details
print("Car 1 Details")
car1.display_car_details()

print("Car 2 Details")
car2.display_car_details()