import re
import csv
from pymongo import MongoClient
import os

# Connect Database 
client = MongoClient("mongodb+srv://samkit:umjtCNkj65nVUct9@cluster0.vbtql.mongodb.net/ReuterDb?retryWrites=true&w=majority")
db = client.ReuterDb

# Read two files 
file = open("reut2-009.sgm","r")
file1 = open("reut2-014.sgm","r")
newfilelines = ''
for line in file:
	newfilelines += line

for line in file1:
    newfilelines += line
    
# List to store all body tag, title tag and dateline tags
body_texts = re.compile('<BODY>(.*?)</BODY>', re.DOTALL).findall(newfilelines)
title_texts = re.compile('<TITLE>(.*?)</TITLE>', re.DOTALL).findall(newfilelines)
dateline_texts = re.compile('<DATELINE>(.*?)</DATELINE>',re.DOTALL).findall(newfilelines)

count = 0
length = len(body_texts)
body= ""

# This loop will add all data into the database
for i in range(length):

    body= body_texts[i]
    
    # Data cleaning for body
    body = body.replace(" Reuter\n&#3;", "");
    body = body.replace(",", "");
    body = body.replace("\n", " ");
    body = body.replace("\s+"," ")
    title = title_texts[i]
    dateline = dateline_texts[i]
    dateline = dateline.replace('\s+',' ')
    dateline = dateline.replace(",", "");
    dateline = dateline.replace("\n", " ");
    print(dateline)
    row = {};
    row['BODY'] =  body;
    row['TITLE'] = title;
    row['DATELINE'] = dateline;
    article_id = db.Articles.insert_one(row).inserted_id
    count = count + 1
    
print("Total:",count)
