#Task1
class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed


# Створення об'єкта класу Car
my_car = Car("Toyota", "Camry", 2020)

# Виконання методу accelerate п'ять разів
for _ in range(5):
    my_car.accelerate()
    print(f"Поточна швидкість: {my_car.get_speed()} км/год")

# Виконання методу brake п'ять разів
for _ in range(5):
    my_car.brake()
    print(f"Поточна швидкість: {my_car.get_speed()} км/год")

    #Task2
    class Buffer:
        def __init__(self):
            self.buffer = []

        def add(self, *a):
            """Додає наступну частину послідовності до буфера."""
            self.buffer.extend(a)

            while len(self.buffer) >= 5:
                sum_five = sum(self.buffer[:5])
                print(f"Сума перших 5 елементів: {sum_five}")
                self.buffer = self.buffer[5:]

        def get_current_part(self):
            """Повертає збережені елементи послідовності."""
            return self.buffer



    my_buffer = Buffer()
    my_buffer.add(1, 2, 3)
    my_buffer.add(4, 5, 6, 7, 8, 9)
    my_buffer.add(10, 11)
    print(f"Поточні елементи буфера: {my_buffer.get_current_part()}")

    #Task2
    class Buffer:
        def __init__(self):
            self.buffer = []

        def add(self, *a):
            """Додає наступну частину послідовності до буфера."""
            self.buffer.extend(a)

            while len(self.buffer) >= 5:
                sum_five = sum(self.buffer[:5])
                print(f"Сума перших 5 елементів: {sum_five}")
                self.buffer = self.buffer[5:]  # Видаляємо вже оброблені елементи

        def get_current_part(self):
            """Повертає збережені елементи послідовності."""
            return self.buffer


    # Приклад використання
    my_buffer = Buffer()
    my_buffer.add(1, 2, 3)
    my_buffer.add(4, 5, 6, 7, 8, 9)
    my_buffer.add(10, 11)
    print(f"Поточні елементи буфера: {my_buffer.get_current_part()}")  # Виведе [10, 11]