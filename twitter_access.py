import tweepy


consumer_key ="IJ3FlcL64zUYm66Xyji3BqSzq"
consumer_secret="quWqYwWAmmlQTNeYE7Qzk2A1e78TQh5yf3j2gUG5JQmAHIRMCS"

access_token="926094950176980992-Hs6zAz0hHe0sai3GZNQL7fI7HypTQ6l"
access_token_secret="5dJIxoHMBHfX4XipnC3JHf0JlT1Vrqbw6cZConU7Fu2Rm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)