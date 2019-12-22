import json

# some JSON
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y["city"])

# Convert from Python to JSON
t = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
z = json.dumps(t)
print(z)
##########################################
k = {
    "name": "Johan",
    "age": 30,
    "Married": True,
    "divorced": False,
    "children": ("ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(k, indent=4, separators=(". ", " = ")))
