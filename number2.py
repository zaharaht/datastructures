keys = ['S001', 'S002', 'S003', 'S004']
values1 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
values2 = [85, 98, 89, 92]

nested_dict = []

for i in range(len(keys)):
    inner_dict = {keys[i]: {values1[i]: values2[i]}}
    nested_dict.append(inner_dict)

print(nested_dict)