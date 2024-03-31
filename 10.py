count = 0
previoustemp = float(input("Введите температуру: "))
currenttemp = float(input("Введите температуру: ")) #та темп. которая = 0 в итоге (маркер)

while currenttemp != 0:
    if currenttemp < previoustemp:
        count += 1
    previoustemp = currenttemp
    currenttemp = float(input("Введите температуру: "))

print("Количество раз, когда температура уменьшилась: ", count)