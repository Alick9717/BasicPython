start_list = [3, 3, 3, 7, 33, 1, 44, 44, 3, 3, 10, 7, 4, 11]
new_list = [i for i in start_list if start_list.count(i) == 1]
print(new_list)