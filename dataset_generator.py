#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:25:34 2020

@author: meetmehta
"""


import os
import pandas as pd
import tweepy
import re
import string
from textblob import TextBlob
import preprocessor as p
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
consumer_key = 'KDCJwQXtknQhZWqjvLaBt8isv'
consumer_secret = 'plXpB6788VI88ZREXqbEFuUubOL7E6IQzKP5zGmlxtInlQGxMY'
access_key= '841435028-Bsa3EQEfAxGBW088S16VwStqbLfqeLUl1c5CV0DA'
access_secret = 'YW7GIAnn1apcHlmUs6xnquNMaDvGgK3InrHhOkkFtkxVN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

COLS = ['positive','negative','subjective','objective','favorite_count', 'followers_count','friends_count','len_tweet','retweet_count', 'no_of_hashtags',
        'no_of_user_mentions','viral_notviral']

start_date = '2016-01-01'
end_date = '2020-03-01'


emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

emoticons = emoticons_happy.union(emoticons_sad)

def clean_tweets(tweet):
    
    stop_words=set(stopwords.words('english'))
    word_tokens=word_tokenize(tweet)
    tweet=re.sub(r':','',tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
    tweet=emoji_pattern.sub(r'',tweet)
    
    
    filtered_tweet=[w for w in word_tokens if not w in stop_words]
    filtered_tweet=[]
    
    for w in word_tokens:
        
        if w not in stop_words and w not in emoticons and w not in string.punctuation :
            
            filtered_tweet.append(w)
            
    return ' '.join(filtered_tweet)


def write_tweets(keyword,file):
    
    if os.path.exists(file):
        
        df=pd.read_csv(file,header=0)
    else:
        df=pd.DataFrame(columns=COLS)
    
    for page in tweepy.Cursor(api.search,q=keyword,count=10000000,include_rts=False,since=start_date).pages(10000000000):
        
        for status in page:
           # print(status['friends_count'])
            new_entry=[]
            status=status._json
           # print(status['user']['friends_count'])
            
            if status['lang']!='en':
                continue
            '''
            if status['created_at'] in df['created_at'].values:
                
                i = df.loc[df['created_at'] == status['created_at']].index[0]
                if status['favorite_count'] != df.at[i, 'favorite_count'] or \
                   status['retweet_count'] != df.at[i, 'retweet_count']:
                    df.at[i, 'favorite_count'] = status['favorite_count']
                    df.at[i, 'retweet_count'] = status['retweet_count']
                continue'''
            
            clean_text=p.clean(status['text'])
            
            filtered_tweet= clean_tweets(clean_text)
            
            blob=TextBlob(filtered_tweet)
            Sentiment=blob.sentiment
            
            
            polarity=Sentiment.polarity
            if (polarity<=0.0):
                new_entry+=[0,1]
            else:
                new_entry+=[1,0]
            subjectivity=Sentiment.subjectivity
            if(subjectivity<0.5):
                new_entry+=[0,1]
            else:
                new_entry+=[1,0]
            
            hashtags = ", ".join([hashtag_item['text'] for hashtag_item in status['entities']['hashtags']])
            mentions = ", ".join([mention['screen_name'] for mention in status['entities']['user_mentions']])
            
            if int(status['retweet_count'])>500:
                viral=1
            else:
                viral=0
            
            new_entry += [int(status['favorite_count']),int(status['user']['followers_count']),int(status['user']['friends_count']), len(status['text']),int(status['retweet_count']),len(hashtags),len(mentions),viral]

            
            
            
           # new_entry.append(hashtags)
            
           # new_entry.append(mentions)
            single_tweet_df = pd.DataFrame([new_entry], columns=COLS)
            df = df.append(single_tweet_df, ignore_index=True)
            csvFile = open(file, 'a' ,encoding='utf-8')
    
    df.to_csv(csvFile, mode='a', columns=COLS, index=False, encoding="utf-8")




    

election_keywords = 'trending OR NarendraModi OR BJP or IndianNationalCongress OR RahulGandhi OR Election2019 OR COVID19'

file='/Users/meetmehta/Desktop/Web_Scrapping/trending_final.csv'

write_tweets(election_keywords, file)
     
df=pd.read_csv('/Users/meetmehta/Desktop/Web_Scrapping/trending_final.csv',header=0)
    
    
    
