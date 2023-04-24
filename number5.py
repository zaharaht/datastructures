def unique_numbers(numbers):
    # convert the list to a set to remove duplicates
    unique_set = set(numbers)
    return unique_set

# example usage
my_list = [1, 2, 3, 2, 4, 5, 3, 6]
unique_numbers_set = unique_numbers(my_list)
print(unique_numbers_set)