from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import logging
import pymongo
import sys

uri = "mongodb+srv://shreyashsingh1:Lookinto1234@cluster0.cihs6do.mongodb.net/"
client = pymongo.MongoClient(uri)
db = client["Scrapper"]
collection_scrapper = db["Reviews"]

# Set the encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(filename="scrapper.log" , level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = urlopen(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

                except:
                    logging.info("name")

                try:
                    rating = commentbox.div.div.div.div.text

                except:
                    rating = 'No Rating'
                    logging.info("rating")


                try:
                    commentHead = commentbox.div.div.div.p.text

                except:
                    commentHead = 'No Comment Heading'
                    logging.info(commentHead)
                    
                    
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text
                    
                except Exception as e:
                    logging.info(e)

                mydict = {
                    "Product": searchString, 
                    "Name": name, 
                    "Rating": rating, 
                    "CommentHead": commentHead, 
                    "Comment": custComment
                }
                reviews.append(mydict)
                
            logging.info("log my final result {}".format(reviews))
            collection_scrapper.insert_many(reviews)  
            
            return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
        
        except Exception as e:
            logging.info(e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
