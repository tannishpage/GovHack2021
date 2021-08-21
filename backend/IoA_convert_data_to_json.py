import requests
import json

# Example of getting data
r = requests.get("https://hackathonapi.moretonbay.qld.gov.au/?Resource=CLIMATE")
print(r.status_code)
j = []
length = len(r.text.split("\r\n"))
print(length)
for i in range(0, length):
    dictionary = {}
    if i / 500 == 1:
        print(i)
        break
    l = r.text.split("\r\n")[i].replace("{", "").replace("}", "").split(",")
    for x in l:
        vals = x.split(":")
        key, value = vals[0].replace("\"", ""), vals[1].replace("\"", "")
        if key == "TIMESTAMP":
            value = value.replace("\\", "")
        dictionary[key] = value
    j.append(dictionary)

api_data = open("MyData.json", "w")
b = json.dumps(j)
json.dump(b, api_data, indent = 4)
