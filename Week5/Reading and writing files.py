import json
"""
Write -> json.dump()
Read -> json.load()
"""

dict1 = {
    "name": "Shreyash",
    "mail_id": "shreyash@gmail.com",
    'phone_no': 9969109851,
    "Subject": ["Data Science", "Big Data", "Data analytics"]
}

with open("data.json", "w") as f:
    json.dump(dict1, f, indent=4)

with open("data.json", "r") as f:
    data = json.load(f)
    print(data["Subject"][1])

with open("data.json", "w") as f:
    json.dump(dict1, f, indent=4)

"""CSV"""
import csv

data = [
    ["name", "email_id", "Phone"],
    ["Shreyash", "shreyashsingh865@gmail.com", "9969109851"],
    ["Ansh", "solankiansh@gmail.com", "7382831092"]
]


with open("data.csv", "w") as f:
     writer_obj = csv.writer(f)
     for i in data:
         writer_obj.writerow(i)

with open("data.csv", "r") as f:
    read_data = csv.reader(f)
    for i in read_data:
        print(i)

with open("data.bin", "wb") as f:
    f.write(b"010101")

with open("data.bin", "rb") as f:
    print(f.read())
