from TwitterAPI import TwitterAPI
import random
import schedule
import time

def job():
    with open('tweets.txt') as file:
        TWEETS = file.readlines()
    CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
    CONSUMER_SECRET = 'XXXXXXXXXXXXXXXX'
    ACCESS_TOKEN_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


    api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

    randomA = random.randint(0, len(TWEETS)-1)

    TWEET_TEXT = TWEETS[randomA]
    r = api.request('statuses/update', {'status': TWEET_TEXT})

    if r.status_code == 200:
        print "Tweeted:", TWEET_TEXT
    else:
        print "FAILURE!"

print "-----------------------------------"
print "            TWEET BOT"
print "-----------------------------------"
print "Waiting...."
schedule.every(30).minutes.do(job)

"""
Soz, I want a free T-shirt for hacktoberfest
"""

while True:
    schedule.run_pending()
    time.sleep(1)
