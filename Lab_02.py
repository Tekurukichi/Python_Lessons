import math
#Task1
a1 = float(input("Введіть першу сторону першого прямокутника: "))
b1 = float(input("Введіть другу сторону першого прямокутника: "))
a2 = float(input("Введіть першу сторону другого прямокутника: "))
b2 = float(input("Введіть другу сторону другого прямокутника: "))
a3 = float(input("Введіть першу сторону третього прямокутника: "))
b3 = float(input("Введіть другу сторону третього прямокутника: "))
S1 = a1 * b1
S2 = a2 * b2
S3 = a3 * b3
print("Площа першого прямокутника:", S1)
print("Площа другого прямокутника:", S2)
print("Площа третього прямокутника:", S3)

#Task2
def hypotenuse(a, b):
  return math.sqrt(a**2 + b**2)

a1 = float(input("Введіть довжину першого катета першого трикутника: "))
b1 = float(input("Введіть довжину другого катета першого трикутника: "))
a2 = float(input("Введіть довжину першого катета другого трикутника: "))
b2 = float(input("Введіть довжину другого катета другого трикутника: "))

hypotenuse1 = hypotenuse(a1, b1)
hypotenuse2 = hypotenuse(a2, b2)

if hypotenuse1 > hypotenuse2:
  print("Гіпотенуза першого трикутника більша за гіпотенузу другого трикутника.")
elif hypotenuse1 < hypotenuse2:
  print("Гіпотенуза другого трикутника більша за гіпотенузу першого трикутника.")
else:
  print("Гіпотенузи двох трикутників рівні.")

#Task3
def is_inside_circle(x, y, a, b, R):
  """Перевіряє, чи лежить точка (x, y) всередині кола."""
  distance = math.sqrt((x - a)**2 + (y - b)**2)
  return distance < R
a = float(input("Введіть координату a центру кола: "))
b = float(input("Введіть координату b центру кола: "))
R = float(input("Введіть радіус кола: "))
p1 = float(input("Введіть координату x точки P: "))
p2 = float(input("Введіть координату y точки P: "))
f1 = float(input("Введіть координату x точки F: "))
f2 = float(input("Введіть координату y точки F: "))
l1 = float(input("Введіть координату x точки L: "))
l2 = float(input("Введіть координату y точки L: "))
inside_count = 0
if is_inside_circle(p1, p2, a, b, R):
  inside_count += 1
if is_inside_circle(f1, f2, a, b, R):
  inside_count += 1
if is_inside_circle(l1, l2, a, b, R):
  inside_count += 1
print("Кількість точок, що лежать всередині кола:", inside_count)

#Task4
X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони T: "))

area_XYZ = 0.5 * X * Y
XZ = math.sqrt(X**2 + Y**2)

if XZ + Z > T and XZ + T > Z and Z + T > XZ:
    # Обчислення площі за формулою Герона
    s = (XZ + Z + T) / 2
    area_XZT = math.sqrt(s * (s - XZ) * (s - Z) * (s - T))
else:
    print("Задані сторони не утворюють трикутник.")
    area_XZT = 0

area = area_XYZ + area_XZT

print("Площа чотирикутника:", area)

#Task5
n = int(input("Введіть натуральне число n: "))
divisors = []
while True:
  divisor = int(input("Введіть число-дільник (введіть 0, щоб завершити): "))
  if divisor == 0:
    break
  divisors.append(divisor)
result = []
for i in range(1, n + 1):
  is_divisible = True
  for divisor in divisors:
    if i % divisor != 0:
      is_divisible = False
      break
  if is_divisible:
    result.append(i)
print("Натуральні числа, що не перевищують", n, "і діляться на всі введені числа:", result)