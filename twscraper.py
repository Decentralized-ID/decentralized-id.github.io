# -*- coding: utf-8 -*-

import tweepy
import csv
import os

#### Credentials

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_KEY')
access_token_secret = os.environ.get('ACCESS_SECRET')

#### Authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#### Keywords
keywords = ["#verifiablecredentials","#selfsovereignidentity","Self+Sovereign+Identity","Hyperledger+Aries","DIDComm","Key+Event+Receipt+Infrastructure","#ToIP","#TrustoverIP","w3c+Credentials"]

#### Get Date
from datetime import date, timedelta, datetime

#### Find 7 Days Ago
current_date = date.today()   
days_before = (date.today()-timedelta(days=7))
now = datetime.now()
date_time = current_date.strftime("%Y-%m-%d")
startDate = days_before.strftime("%Y-%m-%d, %H:%M:%S")


#### Open CSV + Write Column Names
fname = '_data/twitter/search_' + date_time + '.csv'
csvFile = open(fname, 'w+')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Time","Link", "Urls", "UrlTitle", "UrlDesc", "UrlImg", "ImageUrls", "ReplyURL", "QuoteID", "QuoteImg", "QuoteUrl"])
lines_seen = []
text_seen = []
tweet_ids = []

for keyword in keywords:
    # Search hashtags\keywords
    for tweet in tweepy.Cursor(api.search,q=keyword + ' -filter:retweets', count=100, tweet_mode="extended", lang="en", since=days_before).items():
        ### Reset Variables
        medias = []
        lnks = []
        replink = ""
        title = []
        description = []
        image = []
        qtid = ''
        qttext = ''
        qtmedia = ['']
        qturls = ['']
        seen = 'FALSE'

        ### Set basic tweet attributes
        username = tweet.user.screen_name
        id = "https://twitter.com/" + username + "/status/" + tweet.id_str
        idstr = tweet.id_str
        text = tweet.full_text
        created = str(tweet.created_at)

        #### Only add line to csv if it's not already been added
        if hasattr(tweet, 'quoted_status'):
            quotedid = 'https://twitter.com/' + tweet.quoted_status.user.screen_name + '/status/' + tweet.quoted_status_id_str
            if quotedid in lines_seen:
                seen = 'TRUE'
        for y in lines_seen:
            if id == y:
                seen = 'TRUE'
        for q in text_seen:
            if text == q:
                seen = 'TRUE'
        if seen == 'TRUE': continue
        else:
            ### Keep track of seen lines \ tweets
            lines_seen.append(id)
            text_seen.append(text)
            ### Check for reply id
            try:
                reply = tweet.in_reply_to_status_id_str
                user = tweet.in_reply_to_user_id_str
                replink = "https://twitter.com/" + user + "/" + reply
            except:
                pass
            ### Check for images in tweet
            if 'media' in tweet.entities:
                for media in tweet.extended_entities['media']:
                    medias.append(media['media_url_https'])
            ### Check for urls in tweet
            if 'urls' in tweet.entities:
                for url in tweet.entities['urls']:
                    lkn = url['expanded_url']
                    lnks.append(url['expanded_url'])
                    ### Look for metadata
                    from webpreview import web_preview
                    ### Unless link is an image pdf twitter or insta
                    if 'twitter.com' in lkn or '.png' in lkn or '.jpg' in lkn or '.pdf' in lkn or 'instagram.com' in lkn or 'linkedin.com' in lkn or 'facebook.com' in lkn: pass
                    else:
                        try:
                        ### get title img description
                            print('>>Getting Link Metadata<<')
                            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                            tit, desc, ima = web_preview(lkn,timeout=10,headers=headers,parser='lxml')
                            title.append(tit)
                            description.append(desc)
                            image.append(ima) 
                        except:
                            pass
                ### If it's a quote-tweet, get original stats
            if hasattr(tweet, 'quoted_status'):
                qtmedia = ['']
                qturls = ['']
                qttext = tweet.quoted_status.full_text
                qtuser = tweet.quoted_status.user.screen_name
                qtid = "https://twitter.com/" + qtuser + "/status/" + tweet.quoted_status.id_str
                if 'media' in tweet.quoted_status.entities:
                    for media in tweet.quoted_status.extended_entities['media']:
                        qtmedia.append(media['media_url_https'])
                if 'urls' in tweet.quoted_status.entities:
                    for url in tweet.quoted_status.entities['urls']:
                        qturls.append(url['expanded_url'])
            #### Column attributes
            line = [created, id, lnks, title, description, image, medias, replink, qtid, qtmedia, qturls]

            #### Write row to CSV and print line
            csvWriter.writerow(line)
            tweet_ids.append(idstr)
            print(idstr)

#### Get USER Tweets
tweets = []
ids = []
tmpTweets = api.user_timeline('DecentralizeID')
for tweet in tmpTweets:
    created = tweet.created_at.strftime("%Y-%m-%d, %H:%M:%S")
    if created < date_time and created > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at.strftime("%Y-%m-%d, %H:%M:%S") > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        createdate = tweet.created_at.strftime("%Y-%m-%d, %H:%M:%S")
        if createdate < date_time and createdate > startdate:
            tweets.append(tweet)


for tweet in tweets:
    created = str(tweet.created_at)
    id = "https://twitter.com/" + username + "/status/" + tweet.id_str
    idstr = str(tweet.id_str)
    username = tweet.user.screen_name
    if hasattr(tweet, 'text'):
        text = tweet.text
    if hasattr(tweet, 'full_text'):
        text = tweet.full_text
    try: 
        username = tweet.retweeted_status.user.screen_name
        id = "https://twitter.com/" + tweet.retweeted_status.user.screen_name + "/status/" + tweet.retweeted_status.id_str
        idstr = tweet.retweeted_status.id_str
    except:
        pass
    if id not in ids:
        ids.append(id)
        tweet_ids.append(idstr)
        line = [created, id, lnks, title, description, image, medias, replink, qtid, qttext, qtmedia, qturls]
        #### Write row to CSV and print line
        csvWriter.writerow(line)
csvFile.close()
print(tweet_ids)

# Create Collection
from requests_oauthlib import OAuth1Session
import json
## OAuth vs Tweepy auth, idk why can't create collection with above tweepy auth
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_KEY')
access_token_secret = os.environ.get('ACCESS_SECRET')
print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)
twitter = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

# create
url = 'https://api.twitter.com/1.1/collections/create.json'
params_create = {
    'name': 'Decentralized-ID Curated ' + date_time,
    'description': 'Decentralized Identity Curated Tweets by @infominer33 via identosphere.net',
    'timeline_order': 'tweet_chron'
    }
r = twitter.post(url, data=params_create)
print(r.json())
print(r.json()['response'])
# 'response': {'timeline_id': 'custom-1180945428222595074'}}
## Extract ID from response
res = str(r.json()['response'])
ss1 = "{'timeline_id': 'custom-"
ss2 = "'}"
resp = res.removeprefix(ss1)
response = resp.removesuffix(ss2)

timeline_id = r.json()['response']['timeline_id']
# the collection can be viewed at, eg: https://twitter.com/laurenfratamico/timelines/1180945428222595074

# bulk add
url = 'https://api.twitter.com/1.1/collections/entries/curate.json'
# split into batches of 100 for the uploads
n = 100
batches = [tweet_ids[i:i + n] for i in range(0, len(tweet_ids), n)]
print (len(batches))

for batch in batches:
    params_add = {
        "id": timeline_id,
        "changes": []
    }
    for tweet_id in batch:
        sub_params_add = {
            "tweet_id": str(tweet_id),
            "op": "add"
        }
        params_add['changes'].append(sub_params_add)
    
    r = twitter.post(url, data=json.dumps(params_add))
    print(r.json())

file_name = "_posts/twitter/" + str(date_time) + '-twitter.md'
f = open(file_name,"w+")

str1 = "---\n"
str2 = 'title: "Twitter Collection – ' + date_time + '"\n'
str3 = 'description: "Collection of tweets on decentralized identity – ' + date_time + '"\n'
str4 = "last_modified_at: " + date_time + '\n'
str5 = "---\n"
str6 = "\n\n"
str7 = '<a class="twitter-timeline" href="https://twitter.com/DecentralizeID/timelines/' + response + '">Decentralized Identity - Curated ' + date_time + '</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

L = [str1, str2, str3, str4, str5, str6, str7] 
f.writelines(L)
f.close()