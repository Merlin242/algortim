#1
class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade


student1 = Student("Иван", 20, 4.5)
print(student1.name, student1.age, student1.average_grade)

#2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle1 = Rectangle(5, 3)
print(rectangle1.area(), rectangle1.perimeter())
#3
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}, Пробег: {self.mileage} км"

car1 = Car("Toyota", "Camry", 2020, 35000)
print(car1.display_info())
#4
class BankAccount:
    def __init__(self, client_name, balance=0):
        self.client_name = client_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Пополнено {amount} долларов. Новый баланс: {self.balance} долларов."
        else:
            return "Сумма пополнения должна быть положительной."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Снято {amount} долларов. Новый баланс: {self.balance} долларов."
        elif amount > self.balance:
            return "Недостаточно средств на счете."
        else:
            return "Сумма снятия должна быть положительной и не превышать баланс."


account1 = BankAccount("Иванов Иван")
print(account1.deposit(100))
print(account1.withdraw(50))

car1 = Car("Toyota", "Camry", 2020, 35000)
print(car1.display_info())
#5
import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def determine_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний треугольник"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area


triangle1 = Triangle(3, 4, 5)
print(triangle1.determine_type(), triangle1.calculate_area())

triangle2 = Triangle(5, 5, 5)
print(triangle2.determine_type(), triangle2.calculate_area())


