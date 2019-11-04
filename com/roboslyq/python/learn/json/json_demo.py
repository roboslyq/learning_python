import json

""" 
直接将 list保存到json文件中 ，文件的 形式还是list  
"""
data_list = [1, 2, 3, 4, 5, 6, ]
with open("data.json", "w") as data_json:
    jsonObj = json.dump(data_list, data_json)

"""
将标准的 Key-value形式保存的json文件中，文件的具体格式为标准的json
exp:
{
  "phone": "110",
  "info": {
    "id": "01",
    "name": "roboslyq"
  }
}
"""
user_info = {"id": "01", "name": "roboslyq"}
data_info = {"phone": "110", "info": user_info}

with open("user.json", "w") as user_info:
    json.dump(data_info, user_info)
