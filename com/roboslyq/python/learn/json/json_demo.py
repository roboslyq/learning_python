import json

data_list = [1, 2, 3, 4, 5, 6, ]
with open("data.json", "w") as data_json:
    jsonObj = json.dump(data_list, data_json)

user_info = {"id": "01", "name": "roboslyq"}
data_info = {"phone": "110", "info": user_info}
"""
{
  "phone": "110",
  "info": {
    "id": "01",
    "name": "roboslyq"
  }
}
"""
with open("user.json", "w") as user_info:
    json.dump(data_info, user_info)
