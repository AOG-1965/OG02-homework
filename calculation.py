a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

def divide(a, b):
    if b == 0:
        return "Деление на ноль невозможно!"
    return a / b

result = divide(a, b)
print(f"Результат деления: {result}")
