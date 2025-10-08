import requests
import json

# Get the key name from CLI
key_to_find = input("Enter the key you want to find: ")

# Create JSON data from the API

r = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata')
data = r.json()

# Search for the key in JSON
if "meals" in data:
    meal = data["meals"][0]  # get the first data
    if key_to_find in meal:
        print(f"\nValue for '{key_to_find}':\n")
        print(meal[key_to_find])
    else:
        print(f"\nKey '{key_to_find}' not found in the meal data.")
else:
    print("No 'meals' found in the API.")
