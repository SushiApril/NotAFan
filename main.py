

file1 = 'followers_1.json'
file2= 'following.json'


import json
file = 'trial.json'


def get_set(file):
    with open(file,'r') as file:
        data = json.load(file)  # Use json.load() to read the JSON from a file
    new_set = set()
    for item in data:
        for string_data in item.get("string_list_data", []):
            new_set.add(string_data["value"])
    return new_set

def get_set_2(file):
    with open(file,'r') as file:
        data = json.load(file)  # Use json.load() to read the JSON from a file
    new_set = set()
    relationships_following = data.get("relationships_following", [])
    for item in relationships_following:
        for string_data in item.get("string_list_data", []):
            new_set.add(string_data["value"])
    return new_set

x = get_set(file1)
y = get_set_2(file2)
#
final = y-x
print(final)
