import snscrape.modules.twitter as sn
import csv
from datetime import datetime
#Useful properties of returned tweet:
#url: str
#date: datetime.datetime
#rawContent: str aka text
#replyCount: int
#retweetCount: int
#likeCount: int
#quoteCount: int
#See snscrape.modules.twitter.Tweet for full list
def get_tweets(query:str,count:int)->list:
    """Returns tweets based on query for [count] times"""
    data = []
    for i, tweet in enumerate(sn.TwitterSearchScraper(query="lang:en",top=True).get_items()):
        if i >count:
            break
        data.append([tweet.url, tweet.date, tweet.rawContent, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount])
    return data

def get_tweets_as_csv(query:str,count:int):
    """Returns tweets from query [count] times as csv file"""
    with open(str(datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".csv"),"w+", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerows(get_tweets(query,count))
    


