import tweepy
import csv
import pandas as pd

#### Credentials
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

#### Authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#### Keywords
keywords = ['#SelfSovereignIdentity', '#DecentralizedIdentity', '#decentralizedidentity', "#IIW"]

#### Get Date
from datetime import date, timedelta, datetime

#### Find 7 Days Ago
current_date = date.today()   
days_before = (date.today()-timedelta(days=7))
now = datetime.now()
date_time = current_date.strftime("%m%d%y")

#### Open CSV + Write Column Names
fname = 'ssitw' + date_time + '.csv'
csvFile = open(fname, 'w+')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Time", "Link", "Text", "Hashtags", "User", "Favorites", "Following", "Followers", "Retweets", "Urls", "UrlTitle", "UrlDesc", "UrlImg", "ImageUrls", "ReplyURL","QuoteID","QuoteText","QuoteImg","QuoteUrl"])

for keyword in keywords:
    for tweet in tweepy.Cursor(api.search,q=keyword + '-filter:retweets',count=100, tweet_mode="extended", lang="en", since=days_before).items():
        medias = []
        lnks = []
        replink = ""
        rtsr = []
        title = []
        description = []
        image = []
        qtid = ''
        qttext = ''
        qtmedia = ['']
        qturls = ['']

        retweetcount = tweet.retweet_count
        favorites = tweet.favorite_count
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        username = tweet.user.screen_name
        id = "https://twitter.com/" + username + "/status/" + tweet.id_str
        print(id)
        text = tweet.full_text
        print(tweet.full_text)
        hashtags = [hashtag['text'] for hashtag in tweet.entities["hashtags"]]     
        created = tweet.created_at
        print(hashtags)
        try:
            reply = tweet.in_reply_to_status_id_str
            user = tweet.in_reply_to_user_id_str
            replink = "https://twitter.com/" + user + "/" + reply
            print(reply)
        except:
            print("no reply url")
        if 'media' in tweet.entities:
            for media in tweet.extended_entities['media']:
                print(media['media_url_https'])
                medias.append(media['media_url_https'])
        if 'urls' in tweet.entities:
            for url in tweet.entities['urls']:
                print(url['expanded_url'])
                lnks.append(url['expanded_url'])
                quoted = 'FALSE'
                if hasattr(tweet, 'quoted_status'):
                    qtuser = tweet.quoted_status.user.screen_name
                    qtid = "https://twitter.com/" + username + "/status/" + tweet.quoted_status.id_str
                    if qtid == url:
                        quoted = 'TRUE'
                        print("quoted")
                    else:
                        print("notquoted")
                from webpreview import web_preview
                if username == "Docbasia" or quoted == 'TRUE':
                    print("Docbasia")
                else:
                    try:
                        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                        tit, desc, ima = web_preview(url['expanded_url'],timeout=10,headers=headers,parser='lxml')
                        title.append(tit)
                        description.append(desc)
                        image.append(ima) 
                    except:
                        print("broken link")
        # If it's a quote-tweet, get original stats
        if hasattr(tweet, 'quoted_status'):
            qtmedia = ['']
            qturls = ['']
            qttext = tweet.quoted_status.full_text
            print(qttext)
            qtuser = tweet.quoted_status.user.screen_name
            qtid = "https://twitter.com/" + qtuser + "/status/" + tweet.quoted_status.id_str
            if 'media' in tweet.quoted_status.entities:
                for media in tweet.quoted_status.extended_entities['media']:
                    print(media['media_url_https'])
                    qtmedia.append(media['media_url_https'])
            if 'urls' in tweet.quoted_status.entities:
                for url in tweet.quoted_status.entities['urls']:
                    print(url['expanded_url'])
                    qturls.append(url['expanded_url'])
        line = [created, id, text, hashtags, username, favorites, following, followers, retweetcount, lnks, title, description, image, medias, replink, qtid, qttext, qtmedia, qturls]
        lin = "created + ',' + id + ',' + text + ',' + hashtags + ',' + username + ',' + favorites + ',' + following + ',' + followers + ',' + retweetcount + ',' + lnks + ',' + title + ',' + description + ',' + image + ',' + medias + ',' + replink + ',' + qtid + ',' + qttext + ',' + qtmedia + ',' + qturls + '," 
        seen = 'FALSE'
        for row in csvFile:
            if lin == row:
                print("seen")
                seen = 'TRUE'

        if seen == 'TRUE' or username == "Docbasia" :
            print("seen")
        else:
            csvWriter.writerow(line)
            print(line)
csvFile.close()
