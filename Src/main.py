import TwitScrape

for tweet in TwitScrape.get_tweets("lang:en",10):
    print(tweet.rawContent)


