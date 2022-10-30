d = {1: 'опаньки...', 2: 'приветик', 3: 'че как?', 4: 'Россия!'}
key = int(input('Введите ключ, чтобы получить его значение: '))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(d)