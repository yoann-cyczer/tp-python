import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f) 

data["age"] = 31
data["ville"] = "Paris"

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

json_string = json.dumps(data, indent=2, ensure_ascii=False)
print(json_string)
