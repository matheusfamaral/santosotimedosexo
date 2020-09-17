import tweepy
import time

auth = tweepy.OAuthHandler('UQ4Shh8YMEugP7Ea6GQAPhvU8',
                           'gtUAEz8Fv8LajqlVMS6ZIsJRyru0RMvEpMscAhGqFa4R2vATxu')
auth.set_access_token('1306002914125717507-heJfTaupAoEjySX0oiayL8vtAbYoEG',
                      'KrGHa6biUaB1iQzjEBmfcVrUQFkeFB2ZC63GSRnqpIUGZ')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'Santos'
numero = 1000

for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        if((tweet.text)=='Santos'):
            print("nome do usuario: @" + tweet.user.screen_name)
            api.update_status(status="@" + tweet.user.screen_name + " o time do sexo", in_reply_to_status_id=tweet.id)
            print("tweet enviado corretamente")
    except tweepy.TweepError as e:
        time.sleep(30)
        print(e.reason)
    except StopIteration:
        break
