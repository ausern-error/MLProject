import snscrape.modules.twitter as sn
import csv
from datetime import datetime
#returns useful properties of tweets and saves it to a csv file
def get_tweets(query:str,count:int)->list:
    """Returns tweets based on query for count times"""
    data = []
    for i, tweet in enumerate(sn.TwitterSearchScraper(query="lang:en",top=True).get_items()):
        if i >count:
            break
        data.append([tweet.url, tweet.date, tweet.rawContent, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount])

    return data

def get_tweets_as_csv(query:str,count:int):

    with open(str(datetime.now().strftime("%d/%m/%Y_%H:%M:%S") + ".csv"),'w', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerows(get_tweets(query,count))
    


