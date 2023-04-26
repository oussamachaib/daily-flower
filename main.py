import tweepy
from keys import*
import time

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret,access_token, access_token_secret)

client.create_tweet(text = 'This is a test.')
