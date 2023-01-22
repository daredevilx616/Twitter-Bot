import tweepy
import twi_keys
import btc_price
import random
import schedule
import time


def api():
    auth = tweepy.OAuthHandler(twi_keys.api, twi_keys.apiSecret)
    auth.set_access_token(twi_keys.accessToken, twi_keys.accessTokenSecret)

    return tweepy.API(auth)


image_paths = ['btc2.jpg', 'btc3.jpg', 'btc4.jpg', 'btc5.jpg', 'btc6.jpg',
              'btc7.jpg', 'btc8.jpg', 'btc9.jpg', 'btc10.jpg', 'btc11.jpg']


def tweet(api: tweepy.API, message: str):
    if image_paths:
        image_path = random.choice(image_paths)
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted Successfully')


def scheduled_tweet():
    twitter_api = api()
    tweet(twitter_api, 'Highest Bitcoin price of the day: $' + btc_price.max_price +
          '\nLowest Bitcoin price of the day: $' + btc_price.min_price +
          '\n#bitcoin #crypto #btc')

if __name__ == '__main__':
    schedule.every().day.at("00:00").do(scheduled_tweet)
    while True:
       schedule.run_pending()
       time.sleep(1)