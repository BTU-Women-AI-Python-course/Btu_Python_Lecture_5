# Define a class named 'Car'
class Car:
    # Constructor to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display the car's details
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"The engine of the {self.model} is now running!")

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Access the object's attributes
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", my_car.year)

# Call the object's methods
my_car.display_info()
my_car.start_engine()
