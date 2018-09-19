# encoding: utf-8
# Author - Shidong Sun


import tweepy #https://github.com/tweepy/tweepy
import json
import urllib.request
import os

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    # API authoriazation
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    B=int(input('Please input the number of tweets you want to scan(from 20 to 3000):'))
    alltweets = []
    # Make first request of getting tweets, get 10 new tweets and add them to the tweet list
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    alltweets.extend(new_tweets)                   
    # Prevent some extreme conditions that there is no tweet in this account 
    if(alltweets==[]):
        print("NO TWEET AT ALL") 
        return 
    oldest = alltweets[-1].id - 1

    # Repeat the same progress if the first request is successful
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        # Shut the progress when meeting the user's requirement
        if(len(alltweets) >= B):
            break

    media_files = set()
    # Select media file url from all tweets and save them
    # Credit to https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
    # Prevent no-image situiation
    if(media_files==set([])):
        print("No pictures available")
        return
    i=1
    # Download all images into your computer and save them with standard names
    folder=os.getcwd()+'/picture/'
    if not os.path.exists(folder):
        os.makedirs(folder)
    for media_file in media_files:
        urllib.request.urlretrieve(media_file,folder+'%04d'%(i)+'.jpg')
        i+=1
    print("Downloading finish")

if __name__ == '__main__':
    # Pass in the username of the account you want to download
    A=input('Please input the account name you want to download:')
    get_all_tweets(A)
