my_list = [1, 2, 3, 4, 5]
is_sorted = all(my_list[i] <= my_list[i + 1] for i in range(len(my_list) - 1))
print("Is the list sorted?:", is_sorted)
