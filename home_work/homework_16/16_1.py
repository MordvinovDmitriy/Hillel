#!/usr/bin/python3

import json

input_data = {143218: ('Bob', 43),
              234122: ('Alice', 23),
              463211: ('John', 49),
              213521: ('Samantha', 37),
              872432: ('Jack', 55),
              123765: ('Kathryn', 50)}

with open('inp.json', 'w') as file:
    json.dump(input_data, file)
