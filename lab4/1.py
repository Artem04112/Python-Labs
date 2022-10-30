any_list = [1,2,3,3,3,4,5,6,7,7,8,8,9,10,22,33,4,5,6,7,8]
result = []
def odd_index(list):
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    print(result)
odd_index(any_list)