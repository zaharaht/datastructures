import json

# Define the original dictionary
original_dict = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

# Define the name of the JSON file
json_file_name = 'my_json_file.json'

# Write the dictionary to a JSON file
with open(json_file_name, 'w') as json_file:
    json.dump(original_dict, json_file)

# Print the contents of the JSON file
with open(json_file_name, 'r') as json_file:
    json_data = json.load(json_file)
    print(json_data)