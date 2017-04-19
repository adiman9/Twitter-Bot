
from TwitterAPI import TwitterAPI
import random
import schedule
import time

def job():
    CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
    CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCESS_TOKEN_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

    followers = []
    for id in api.request('followers/ids'):
        followers.append(id)


    friends = []
    for id in api.request('friends/ids'):
        friends.append(id)


    non_friends = [friend for friend in friends if friend not in followers]

    for id in non_friends:
        r = api.request('friendships/destroy', {'user_id': id})
        if r.status_code == 200:
            status = r.json()
            print 'unfollowed %s' % status['screen_name']

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
