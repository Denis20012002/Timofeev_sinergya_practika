"""
Модуль для демонстрации принципов ООП: наследования и полиморфизма.
Реализует иерархию классов животных с возможностью расширения.
"""

from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    """Абстрактный базовый класс для всех животных."""

    @abstractmethod
    def speak(self) -> str:
        """Воспроизвести характерный звук животного.

        Returns:
            Строка с описанием звука
        """
        pass

    def get_species(self) -> str:
        """Получить название вида животного.

        Returns:
            Название вида
        """
        return self.__class__.__name__


class Dog(Animal):
    """Класс, представляющий собаку."""

    def speak(self) -> str:
        """Собака лает.

        Returns:
            Строка с лаем собаки
        """
        return "Собака лает: Гав!"


class Cat(Animal):
    """Класс, представляющий кошку."""

    def speak(self) -> str:
        """Кошка мяукает.

        Returns:
            Строка с мяуканьем кошки
        """
        return "Кошка мяукает: Мяу!"


class AnimalFactory:
    """Фабрика для создания животных."""

    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        """Создать животное указанного типа.

        Args:
            animal_type: Тип животного ('dog', 'cat')

        Returns:
            Экземпляр животного

        Raises:
            ValueError: Если передан неизвестный тип животного
        """
        animals = {
            'dog': Dog,
            'cat': Cat
        }

        if animal_type not in animals:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")

        return animals[animal_type]()


def demonstrate_polymorphism(animals: List[Animal]) -> None:
    """Демонстрация полиморфного поведения животных.

    Args:
        animals: Список объектов животных
    """
    print("\nДемонстрация полиморфизма:")
    for i, animal in enumerate(animals, 1):
        print(f"{i}. {animal.get_species()}: {animal.speak()}")


def main() -> None:
    """Основная функция демонстрации работы программы."""
    print("Демонстрация работы классов животных")
    print("=" * 40)

    # Создание животных через фабрику
    try:
        dog = AnimalFactory.create_animal('dog')
        cat = AnimalFactory.create_animal('cat')

        # Демонстрация базовой функциональности
        print("\nБазовый класс Animal (через фабрику):")
        print(f"Собака: {dog.speak()}")
        print(f"Кошка: {cat.speak()}")

        # Демонстрация полиморфизма
        animals = [dog, cat]
        demonstrate_polymorphism(animals)

        # Дополнительная информация
        print(f"\nВсего животных: {len(animals)}")
        for animal in animals:
            print(f"- {animal.get_species()}")

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
