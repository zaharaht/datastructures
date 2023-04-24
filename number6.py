# create the dictionary
capitals = {'USA': 'Washington, D.C.', 'Canada': 'Ottawa', 'Uganda': 'kampala', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 'Japan': 'Tokyo'}

# prompt the user to enter a country name
country = input("Enter a country name: ")

# look up the capital for the entered country
if country in capitals:
    capital = capitals[country]
    print(f"The capital of {country} is {capital}.")
else:
    print(f"Sorry, we don't have information about the capital of {country}.")