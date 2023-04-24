import itertools

# create the dictionary
my_dict = {'1': ['a', 'b'], '2': ['c', 'd']}

# create a list of lists containing the values for each key
values = [my_dict[key] for key in my_dict]

# use itertools.product() to generate all combinations of letters
combinations = list(itertools.product(*values))

# print each combination as a string
for combo in combinations:
    print(''.join(combo))