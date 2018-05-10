import json

with open("users.json","w") as file:
    file.write(json.dumps({"name":"john"}))
json.dumps()
