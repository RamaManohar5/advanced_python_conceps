'''
JSON (JavaScript Object Notation) is a leightweight data format for data exchange. 
In Python you have the built-in json module for encoding and decoding JSON data.
Simply import it and you are ready to work with JSON data:
'''
# From Python to JSON (Serialization, Encode)
# Convert Python objects into a JSON string with the json.dumps() method.
import json

person = {"name": "John",\
           "age": 30,\
              "city": "New York",\
                  "hasChildren": False, \
                    "titles": ["engineer", "programmer"]\
                        }
# converting in to json
person_json  = json.dumps(person)
# use different formatting style 
person_json2 = json.dumps(person, indent=4, separators=(';', '='), sort_keys=False)
print(person_json)
print(person_json2)
# Or convert Python objects into JSON objects and save them into a file with the json.dump() method
with open('person.json', 'w') as f:
    person1 = json.dump(person, f)
    print(person1)

# FROM JSON to Python (Deserialization, Decode)
# Convert a JSON string into a Python object with the json.loads() method. \
# The result will be a Python dictionary.
import json
person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person_json)
print(person)

# Or load data from a file and convert it to a Python object with the json.load() method.

import json
with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)