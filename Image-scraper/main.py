import requests
from bs4 import BeautifulSoup as bs
import logging
from urllib.request import urlopen
import pymongo
import os

query = "Bugatti"

save_dir = 'image/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# Basically it returns the whole html page with the src location of img
response = requests.get(f"https://www.google.com/search?sxsrf=AB5stBjZ_Rhu6v3IeR9VRWPHgpetFCtWZQ:1688480586443&q={query}&tbm=isch&sa=X&ved=2ahUKEwihoMKsoPX_AhVH3TgGHaMHAc0Q0pQJegQIChAB&biw=1536&bih=760&dpr=1.25")
print(response.content)

"""To access the content of the response, the .content attribute is used. 
The .content attribute retrieves the raw binary data of the response, which 
represents the content of the image."""

soup = bs(response.content, "html.parser")
image_tags = soup.find_all("img")

del image_tags[0]

img_data_mongo = []
for i in image_tags:
    img_url = i["src"]
    # Here we get data from google server in return, as we are requesting i.e, img data in binary form
    """To access the content of the response, the .content attribute is used. 
       The .content attribute retrieves the raw binary data of the response, which 
       represents the content of the image."""
    img_data = requests.get(img_url).content
    mydict = {"index": img_url, "image": img_data}
    img_data_mongo.append(mydict)
    with open(os.path.join(save_dir, f"{query}_{image_tags.index(i)}.jpg"), "wb") as f:
        f.write(img_data)
        
uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(uri)
db = client["Img_scraper"]
coll_img = db["Img_collection"]  
coll_img.insert_many(img_data_mongo)
    