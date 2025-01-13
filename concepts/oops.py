# 1. Classes and Objects
print("\n1. Basic Class and Object:")
class Car:
    # Class variable (shared by all instances)
    total_cars = 0
    
    # Constructor (Initializer)
    def __init__(self, brand, model):
        # Instance variables (unique to each instance)
        self.brand = brand
        self.model = model
        self._price = 0  # Protected attribute (convention)
        self.__mileage = 0  # Private attribute
        Car.total_cars += 1
    
    # Instance method
    def start_engine(self):
        return f"{self.brand} {self.model}'s engine is starting"
    
    # Class method
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars
    
    # Static method
    @staticmethod
    def get_company_info():
        return "Car Manufacturer Inc."

# Creating objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
print(f"Total cars: {Car.get_total_cars()}")
print(car1.start_engine())

# 2. Inheritance
print("\n2. Inheritance Examples:")
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} is starting"

class ElectricCar(Vehicle):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)  # Call parent constructor
        self.battery_capacity = battery_capacity
    
    def start(self):  # Method overriding
        return f"{super().start()} silently"

tesla = ElectricCar("Tesla", "75kWh")
print(tesla.start())

# 3. Multiple Inheritance
print("\n3. Multiple Inheritance:")
class Flying:
    def fly(self):
        return "Flying"

class Swimming:
    def swim(self):
        return "Swimming"

class FlyingFish(Flying, Swimming):
    pass

flying_fish = FlyingFish()
print(flying_fish.fly())
print(flying_fish.swim())

# 4. Encapsulation
print("\n4. Encapsulation:")
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(1000)
print(f"Balance: {account.get_balance()}")

# 5. Polymorphism
print("\n5. Polymorphism:")
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)

# 6. Abstract Classes
print("\n6. Abstract Classes:")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print(f"Rectangle Area: {rect.area()}")

# 7. Properties (Getters, Setters, Deleters)
print("\n7. Properties:")
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature()
temp.celsius = 25
print(f"Fahrenheit: {temp.fahrenheit}")

# 8. Magic Methods (Dunder Methods)
print("\n8. Magic Methods:")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)
print(p1 == Point(1, 2))

# 9. Class Composition
print("\n9. Class Composition:")
class Engine:
    def start(self):
        return "Engine started"

class CarWithComposition:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()

car = CarWithComposition()
print(car.start())

# 10. Method Types and Decorators
print("\n10. Method Types:")
class MyClass:
    class_var = 0
    
    def instance_method(self):
        return "Instance method"
    
    @classmethod
    def class_method(cls):
        return "Class method"
    
    @staticmethod
    def static_method():
        return "Static method"
    
    @property
    def my_property(self):
        return "Property value"

obj = MyClass()
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())
print(obj.my_property)
