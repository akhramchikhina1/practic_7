values = input('Введите N, K, R ').split()
N = int(values[0])
K = int(values[1])
R = int(values[2])

day = 1
current_length = N

while current_length < R:
    current_length= current_length* (1 + K / 100)
    day += 1

print(day)