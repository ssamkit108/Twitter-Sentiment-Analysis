from pyspark import SparkContext
from pymongo import MongoClient

def main():
    sparkcontext = SparkContext("local","frequency of words")
          
    words_tweets = getwordlistoftweets()
    words_articles = getwordlistfromarticles()
    totalwords = words_articles + words_tweets
    totalwords = list(map(lambda x:x.lower(),totalwords))
    words_sdd = sparkcontext.parallelize(totalwords)
    counts = words_sdd.map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],False)
    
    print("Frequence of word:")
    counts.foreach(print)

def getwordlistoftweets():
    client = MongoClient("mongodb+srv://samkit:umjtCNkj65nVUct9@cluster0.vbtql.mongodb.net/ProcessedDb?retryWrites=true&w=majority")
    db_processed = client.ProcessedDb

    data = db_processed.tweets
    tweetlist= data.find()
    keywords = ["Storm", "Winter", "Canada", "hot", "cold", "Flu", "Snow", "Indoor", "Safety", "rain", "ice"]
    listofwords=[]
    for row in tweetlist:
        words= row['Content'].split(" ")
        filtered_words = filter(lambda word: word in keywords, words)
        listofwords.extend(list(filtered_words))
    return listofwords

def getwordlistfromarticles():
    client = MongoClient("mongodb+srv://samkit:umjtCNkj65nVUct9@cluster0.vbtql.mongodb.net/ReuterDb?retryWrites=true&w=majority")
    db_articles = client.ReuterDb

    data = db_articles.Articles
    articlelist= data.find()
    keywords = ["Storm", "Winter", "Canada", "hot", "cold", "Flu", "Snow", "Indoor", "Safety", "rain", "ice"]
    listofwords=[]
    for row in articlelist:
        words= row['BODY'].split(" ")
        filtered_words = filter(lambda word: word in keywords, words)
        listofwords.extend(list(filtered_words))
    return listofwords

if __name__ == '__main__':
    main()
