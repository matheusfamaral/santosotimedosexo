import tweepy
import time

consumer_key = 'UQ4Shh8YMEugP7Ea6GQAPhvU8'
consumer_secret = 'gtUAEz8Fv8LajqlVMS6ZIsJRyru0RMvEpMscAhGqFa4R2vATxu'
key =  '1306002914125717507-heJfTaupAoEjySX0oiayL8vtAbYoEG'
secret = 'KrGHa6biUaB1iQzjEBmfcVrUQFkeFB2ZC63GSRnqpIUGZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

search = 'Santos'
numero = 10000000

for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        if((tweet.text)=='Santos'):
            print("nome do usuario: @" + tweet.user.screen_name)
            api.update_status(status="@" + tweet.user.screen_name + " o time do sexo", in_reply_to_status_id=tweet.id)
            print("tweet enviado corretamente")
            time.sleep(30)
    except tweepu.RateLimitError:
        time.sleep(5*60)
    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(30)
    except StopIteration:
        time.sleep(30)
        break
