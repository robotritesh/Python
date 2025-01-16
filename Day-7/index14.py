my_list = [10, 20, 30, 40, 50]
unique_list = list(set(my_list))  # Remove duplicates if any
unique_list.sort()
second_largest = unique_list[-2]
print("Second largest number:", second_largest)
