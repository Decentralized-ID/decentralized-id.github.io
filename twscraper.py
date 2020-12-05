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
keywords = ["#verifiablecredentials","#selfsovereignidentity","Self+Sovereign+Identity","Hyperledger+Aries","DIDComm","Key+Event+Receipt+Infrastructure","#ToIP","#TrustoverIP","w3c+Credentials"]

#### Get Date
from datetime import date, timedelta, datetime

#### Find 7 Days Ago
current_date = date.today()   
days_before = (date.today()-timedelta(days=7))
now = datetime.now()
date_time = current_date.strftime("%m%d%y")

#### Open CSV + Write Column Names
fname = 'SSI-DID_' + date_time + '.csv'
csvFile = open(fname, 'w+')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Time","ID", "Link", "Likes", "Shares", "User", "Text", "Hashtags", "Urls", "UrlTitle", "UrlDesc", "UrlImg", "ImageUrls", "ReplyURL", "QuoteID", "QuoteText", "QuoteImg", "QuoteUrl"])
lines_seen = []
text_seen = []

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
        retweetcount = tweet.retweet_count
        favorites = tweet.favorite_count
        username = tweet.user.screen_name
        id = "https://twitter.com/" + username + "/status/" + tweet.id_str
        idstr = tweet.id_str
        text = tweet.full_text
        hashtags = [hashtag['text'] for hashtag in tweet.entities["hashtags"]]     
        created = str(tweet.created_at)

        #### Only add line to csv if it's not already been added
        if hasattr(tweet, 'quoted_status'):
            quotedid = 'https://twitter.com/' + tweet.quoted_status.user.screen_name + '/status/' + tweet.quoted_status_id_str
            print("Quoted ID " + quotedid)
            if quotedid in lines_seen:
                print("Quoted Status Seen")
                seen = 'TRUE'
        for y in lines_seen:
            if id == y:
                seen = 'TRUE'
        for q in text_seen:
            if text == q:
                seen = 'TRUE'
        if seen == 'TRUE' or username == "Docbasia": continue
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
                print("no reply url")
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
                    if username == "Docbasia" or 'twitter.com' in lkn or '.png' in lkn or '.jpg' in lkn or '.pdf' in lkn or 'instagram.com' in lkn or 'linkedin.com' in lkn or 'facebook.com' in lkn: continue
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
                            print("broken link")
                ### If it's a quote-tweet, get original stats
            if hasattr(tweet, 'quoted_status'):
                print("Quoted Status NotSeen")
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
            line = [created, "'"+idstr+"'", id, favorites, retweetcount, username, text, hashtags, lnks, title, description, image, medias, replink, qtid, qttext, qtmedia, qturls]

            #### Write row to CSV and print line
            csvWriter.writerow(line)
            print(line)
csvFile.close()
print("Complete")