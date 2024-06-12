#Task1
a = int(input("Введіть ціле число для змінної a: "))
b = float(input("Введіть дробове число для змінної b: "))
c = int(input("Введіть ціле число для змінної c: "))
d = float(input("Введіть дробове число для змінної d: "))
print("Змінна a:", a)
print("Змінна b:", b)
print("Змінна c:", c)
print("Змінна d:", d)

#Task2
addition = a + d
subtraction = a - b
multiplication = a * d
division = a / b
exponentiation = c ** b
floor_division = a // b
remainder = a % d
results = [addition, subtraction, multiplication, division, exponentiation, floor_division, remainder]
print("Результати дій:")
print(results)

#Task3
number_of_elements = len(results)
print("Кількість елементів у списку:", number_of_elements)

# Виведення парних елементів
print("Парні елементи списку:")
for element in results:
    if element % 2 == 0:
        print(element)

#Task4
results[1], results[4] = results[4], results[1]

# Виведення отриманого списку
print("Отриманий список:")
print(results)

#Task5
name = input("Введіть ваше прізвище та ім'я: ")

print("Виконавець лабораторної роботи:", name)
print("Висновки по лабораторній роботі:")
print("У цій роботі я навчився:")
print("- Опрацьовувати введення даних від користувача.")
print("- Виконувати арифметичні дії над числами.")
print("- Створення та маніпулювання списками.")
print("- Доступ до елементів списку та їх зміна.")
print("- Виведення даних на екран.")
