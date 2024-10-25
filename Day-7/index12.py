import json

# Convert Python dictionary to JSON
data = {"name": "Alice", "age": 25, "city": "New York"}
json_data = json.dumps(data)
print("JSON Data:", json_data)

# Convert JSON back to Python dictionary
python_data = json.loads(json_data)
print("Python Data:", python_data)
