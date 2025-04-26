from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, (int, float)) or age <= 0:
            raise ValueError("Age must be a positive number.")
        self.__name = name  
        self.__age = age    

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, (int, float)) or age <= 0:
            raise ValueError("Age must be a positive number.")
        self.__age = age

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Chirp! Chirp!"


class ZooManagementSystem:
    def __init__(self):
        self.__animals = []  

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Only objects of type Animal can be added.")
        self.__animals.append(animal)

    def list_animals(self):
        if not self.__animals:
            print("No animals in the zoo.")
        else:
            for animal in self.__animals:
                print(f"Name: {animal.get_name()}, Age: {animal.get_age()}, Sound: {animal.make_sound()}")

if __name__ == "__main__":
    zoo = ZooManagementSystem()

    try:
        dog = Dog("Buddy", 3)
        cat = Cat("Whiskers", 2)
        bird = Bird("Tweety", 1)

        zoo.add_animal(dog)
        zoo.add_animal(cat)
        zoo.add_animal(bird)

        zoo.list_animals()
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")