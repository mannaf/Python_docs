import json

# some JSON
x = '{"name ":"Jason","age":30,"city":"New Yeork"}'
# parse x:
y = json.loads(x)

# the result is a python dictonary
