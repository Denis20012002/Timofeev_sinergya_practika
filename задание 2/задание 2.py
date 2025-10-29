class Animal:
    def speak(self):
        return "Животное издает звук"


class Dog(Animal):
    def speak(self):
        return "Собака лает: Гав!"


if __name__ == "__main__":
    print("Демонстрация работы классов \n")
    animal = Animal()
    dog = Dog()
    print("Базовый класс Animal:")
    print(animal.speak())
    print("\nПроизводный класс Dog:")
    print(dog.speak())
    print("\nПолиморфизм:")
    animals = [animal, dog]
    for a in animals:
        print(a.speak())
