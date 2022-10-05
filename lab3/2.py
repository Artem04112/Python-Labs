numbers = []
for i in input('Вводите числа через пробел: ').split():
    numbers.append(int(i))
num_of_0 = numbers.count(0)
print(num_of_0)