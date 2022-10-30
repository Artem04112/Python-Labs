any_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
def replacement(list):
    i_of_max_el = list.index(max(list))
    i_of_min_el = list.index(min(list))
    list[i_of_max_el], list[i_of_min_el] = list[i_of_min_el], list[i_of_max_el]
    print(list)
replacement(any_list)
