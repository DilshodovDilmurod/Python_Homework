1 Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.PI = 3.14
    def get_perimetr(self):
        return 2*self.PI*self.radius
    def get_area(self):
        return self.PI*self.radius**2

2 Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self, name, country, date_birth):
        self.name = name
        self.country = country
        self.date_birth = date_birth
    def get_age(self, now_year):
        return now_year - self.date_birth

3 Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Claculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 - num2
    def add_func(self):
        return self.num1 + self.num2
    def sub_func(self):
        return self.num1 - self.num2
    def dup_func(self):
        return self.num1 * self.num2
    def devision_func(self):
        return self.num1/self.num2
    
4 Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
class Shakl:
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi
    def get_perimetr(self):
        return 2 * self.eni * self.boyi
    def get_area(self):
        return self.eni * self.boyi
    
class Circle(Shakl):
    def __init__(self, radius):
        self.radius = radius
        self.PI = 3.14
    def get_area(self):
        return self.PI*self.radius**2
    def get_perimetr(self):
        return 2*self.PI*self.radius

class Triangle(Shakl):
    def __init__(self, eni, boyi, balandligi):
        super().__init__(eni, boyi)
        self.balandligi = balandligi
    def get_area(self):
        return (self.boyi+ self.eni)*self.balandligi /2
    def get_perimetr(self):
        return self.balandligi+self.boyi+self.eni
6 Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)
        print(f'{item} stackka qoshildi')
    
    def pop(self):
        if not len(self.items) ==0:
            remove_item = self.items.pop()
            print(f'{remove_item} stackdan olin')
            return remove_item
        else: 
            print('Stack bosh')

7 Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
class Stack:
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)
        print(f'{item} stackka qoshildi')
    
    def pop(self):
        if not len(self.items) ==0:
            remove_item = self.items.pop()
            print(f'{remove_item} stackdan olin')
            return remove_item
        else: 
            print('Stack bosh')

8 Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class Shoping_card:
    def __init__(self):
        self.items =[]

    def add_item(self, name, price):
        self.items.append({'name':name, 'price':price})
        print(f'{name} savatga qoshildi')

    def remove_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                return print(f'{name} savatdan ochirildi')
            else:
                print(f'{name} savatda mavjud emas')
    def total_sale(self):
        total_sale = sum(item['price'] for item in self.items)
        return total_sale

9 Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else: 
            print('Stack bosh')
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else: 
            print('Stack bosh')
            return None

    def is_empty(self):
        return len(self.items) == 0
stack = Stack()
stack.push('salom')
stack.push(30)
stack.push(70)
stack.push(60)
print(stack.peek())
print(stack.pop())
print(stack.peek())
