
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import urllib.request
import os

#Twitter API credentials
consumer_key = "kBERBqyuCHyctgtyRHBEzG7T7"
consumer_secret = "zqzGAYSpf1CHGvLGiwizowRXm0x79MSNE5ycKc7D6aFto8DR7I"
access_key = "1039252610426044417-L7YoZ3Gdfmkag2qW6XQiCVyhn8Ljl3"
access_secret = "zM8Q2asrlMFTVKSsTERUIWr37x3IxOeVQ56Xu8fgKTXDH"


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)

    alltweets.extend(new_tweets)
    if(alltweets==[]):
        print("NO TWEET AT ALL")  
        return  

    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 50):
            break
    media_files = set()
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
##https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
    if(media_files==set([])):
        print("No pictures available")
        return
    i=1
    for media_file in media_files:
        urllib.request.urlretrieve(media_file,'/home/gary/EC601/picture/'+'%04d'%(i)+'.jpg')
        i+=1
    print(" Done")
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@BU_Tweets")
