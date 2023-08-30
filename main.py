# Напишите следующие функции:
#
#  1. Нахождение корней квадратного уравнения
#  2. Генерация csv файла с тремя случайными числами
#  в каждой строке. 100-1000 строк.
#  3. Декоратор, запускающий функцию нахождения корней квадратного
#  уравнения с каждой тройкой чисел из csv файла.
#  4. Декоратор, сохраняющий переданные параметры
#  и результаты работы функции в json файл.


import json
import csv
from random import randint


#  1. Нахождение корней квадратного уравнения

def solve_quadratic(a: float, b: float, c: float) -> list:
    discrim = b**2 - 4 * a * c
    res = []
    if discrim > 0:
        root1 = round((-b - discrim**0.5) / 2 * a, 2)
        root2 = round((-b + discrim**0.5) / 2 * a, 2)
        res.append(root1)
        res.append(root2)
    elif discrim == 0:
        root = -b / 2 * a
        res.append(root)
    else:
        print('Нет корней')

    return res

#  2. Генерация csv файла с тремя случайными числами
#  в каждой строке. 100-1000 строк

MIN_NUM = 1
MAX_NUM = 100
MIN_ROWS = 100
MAX_ROWS = 1000

def generate_random_num():
    return randint(MIN_NUM, MAX_NUM)

def generate_csv_file():
    num_rows = randint(MIN_ROWS, MAX_ROWS)
    data = []
    for _ in range(num_rows):
        row = [generate_random_num() for _ in range(3)]
        data.append(row)

    with open('random_num.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

#  3. Декоратор, запускающий функцию нахождения корней квадратного
#  уравнения с каждой тройкой чисел из csv файла.
def process_csv_data(filename, process_func):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            numbers = [float(num) for num in row]
            process_func(*numbers)

def quadratic_decorator(func):
    def wrapper(a, b, c):
        print(f"Решаем уравнение: {a}x^2 + {b}x + {c} = 0")
        roots = func(a, b, c)
        if roots is None:
            print("Нет корней")
        else:
            print("Корни:", roots)
    return wrapper

@quadratic_decorator
def solve_quadratic_and_print(a, b, c):
    return solve_quadratic(a, b, c)

process_csv_data('random_num.csv', solve_quadratic_and_print)

#  4. Декоратор, сохраняющий переданные параметры
#  и результаты работы функции в json файл.

def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "parameters": args,
                "result": result
            }
            with open(filename, 'a') as jsonfile:
                json.dump(data, jsonfile)
                jsonfile.write('\n')
            return result
        return wrapper
    return decorator

@save_to_json('results.json')
def save_solve_quadratic(a, b, c):
    discrim = b ** 2 - 4 * a * c
    res = []
    if discrim > 0:
        root1 = round((-b - discrim ** 0.5) / 2 * a, 2)
        root2 = round((-b + discrim ** 0.5) / 2 * a, 2)
        res.append(root1)
        res.append(root2)
    elif discrim == 0:
        root = -b / 2 * a
        res.append(root)
    else:
        print('Нет корней')

    return res

