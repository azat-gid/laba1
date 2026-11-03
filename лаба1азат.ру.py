import math

# 1. Запрашиваем у пользователя угол альфа в градусах
alpha_deg = float(input("Введите значение угла альфа (в градусах): "))

# 2. Переводим градусы в радианы для функций модуля math
alpha = math.radians(alpha_deg)

# 3. Вычисление по первой формуле (с проверкой знаменателя)
numerator = math.sin(2 * alpha) + math.sin(5 * alpha) - math.sin(3 * alpha)
denominator = math.cos(alpha) + 1 - 2 * (math.sin(2 * alpha) ** 2)

# Проверяем, не равен ли знаменатель нулю
if abs(denominator) < 1e-9:
    print("Результат z1: Ошибка! Деление на ноль (угол вне ОДЗ первой формулы).")
    z1 = None
else:
    z1 = numerator / denominator
    print(f"Результат z1 = {z1:.6f}")

# 4. Вычисление по второй формуле
z2 = 2 * math.sin(alpha)
print(f"Результат z2 = {z2:.6f}")

# 5. Сравнение результатов (если z1 удалось посчитать)
if z1 is not None:
    if math.isclose(z1, z2, abs_tol=1e-5):
        print("Результаты совпадают!")
    else:
        print("Результаты не совпадают!")