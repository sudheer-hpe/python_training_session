# Topics going to be covered in the assignments:
# 1. Dictionary == JSON
# 2. List.
# 3. Functions.
# 4. Loops.
# 5. I/O operations.

import json

# d = {
#     'key': 'value1',
#     "key2": "value2"
# }

# "r": read mode
# "w": write mode
# "a": append mode
# "r+": read and write mode
# "b": binary mode


def load_json(filename):
    with open(filename, "r") as f: # with open("data_2.json", "r") as f:
        d = json.load(f)
    return d

d = []
filenames = ["data_1.json", "data_2.json", "data_3.json"]
for x in filenames:
    d.append(load_json(x))

while filenames: # while True: 1st iteration, 2nd iteration, 3rd iteration
    x = filenames.pop()
    d.append(load_json(x))
    # filenames = []
# TRUTHY / FALSY
# a = 1
# a == 1 -> True
# a == 2 -> False
# a = [] -> 0
a = []# {}, set(), tuple(), None, "", ''
if a:
    print("hi")
else:
    print("no")