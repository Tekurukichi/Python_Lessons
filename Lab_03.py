from datetime import date

#Task1
class Person:
    def __init__(self, surname, first_name, nickname=None, birth_date_str=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname

        if birth_date_str:
            year, month, day = map(int, birth_date_str.split('-'))
            self.birth_date = date(year, month, day)
        else:
            self.birth_date = None

    def get_age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year
            if today.month < self.birth_date.month or (
                    today.month == self.birth_date.month and today.day < self.birth_date.day):
                age -= 1
            return str(age)
        else:
            return "Немає даних про дату народження"

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"


# Приклад використання
person1 = Person("Іванов", "Іван", "Іванчик", "2002-12-31")
print(person1.get_fullname())  # Виведе: Іванов Іван
print(person1.get_age())  # Виведе: 20 (на 2023-08-17)

person2 = Person("Петрова", "Олена", birth_date_str="1995-05-15")
print(person2.get_fullname())  # Виведе: Петрова Олена
print(person2.get_age())  # Виведе: 28 (на 2023-08-17)

person3 = Person("Сидоров", "Олександр")
print(person3.get_fullname())  # Виведе: Сидоров Олександр
print(person3.get_age())  # Виведе: Немає даних про дату народження

# Task 2: Модифікація файлу
def modifier(filename):
    """Модифікує файл з даними про людей."""
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Створюємо список об'єктів Person
    people = []
    for line in lines:
        surname, first_name, nickname, birth_date = line.strip().split(',')
        people.append(Person(surname, first_name, nickname, birth_date))

    # Додаємо графу повного імені
    modified_lines = []
    for person in people:
        modified_lines.append(
            f"{person.surname},{person.first_name},{person.nickname},{person.birth_date},{person.get_fullname()},{person.get_age()}\n")

    # Записуємо змінені дані в файл
    with open(filename, 'w') as f:
        f.writelines(modified_lines)


# Приклад використання
modifier("contacts.txt")