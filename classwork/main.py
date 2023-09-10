# Класс Машины
class Car:
    # Инициализация атрибутов
    def __init__(self, model, year_manufacture, engine_capacity, cost, mileage):
        self.model = model  # Модель машины
        self.year_manufacture = year_manufacture  # Год выпуска
        self.engine_capacity = engine_capacity  # Объем двигателя
        self.cost = cost  # Стоимость машины
        self.mileage = mileage  # Пробег машины
        self.wheels = 4  # Количество колес

    # Функция вывода описания машины
    def car_description(self):
        print(f"Я машина!! Модель: {self.model}, Год выпуска: {self.year_manufacture}, "
              f"Объем двигателя: {self.engine_capacity}, Стоимость: {self.cost}, Пробег: {self.mileage}, "
              f"Количество колес: {self.wheels}")


# Класс грузовика, потомка класса Машина
class Truck(Car):
    # Инициализация атрибутов
    def __init__(self, model, year_manufacture, engine_capacity, cost, mileage):
        super().__init__(model, year_manufacture, engine_capacity, cost, mileage)
        self.wheels = 8

    # Перегрузка функции вывода описания машины в описание грузовика
    def car_description(self):
        print(f"Я грузовик !! Модель: {self.model}, Год выпуска: {self.year_manufacture},"
              f" Объем двигателя: {self.engine_capacity}, Стоимость: {self.cost}, Пробег: {self.mileage},"
              f" Количество колес: {self.wheels}")


# Создание экземпляра класса машина
car1 = Car("uaz", 1998, 100, 10000, 10000)
# Вывод описания экземпляра машины
car1.car_description()

# Создание экземпляра класса грузовик
truck1 = Truck("uaz2", 1998, 100, 10000, 10000)
# Вывод описания экземпляра грузовика
truck1.car_description()
