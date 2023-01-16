import snscrape.modules.twitter as sn
#hello forgottenrat joined
#Useful properties of returned tweet:
#	url: str
#	date: datetime.datetime
#	rawContent: str aka text
#	replyCount: int
#	retweetCount: int
#	likeCount: int
#	quoteCount: int
#See snscrape.modules.twitter.Tweet for full list

def get_tweets(query:str,count:int)->list:
    """Returns tweets based on query for count times"""
    data = []
    for i, tweet in enumerate(sn.TwitterSearchScraper(query="lang:en",top=True).get_items()):
        if i >count:
            break
        data.append(tweet)
    return data
