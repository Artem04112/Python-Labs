numbers = []
for i in range(0,10):
    for i in input('Вводите числа: ').split():
        numbers.append(int(i))
print(numbers)
print(sum(numbers))