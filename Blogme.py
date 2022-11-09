# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:37:45 2022

@author: shaga
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or excel.xlsx files

data = pd.read_excel('articles.xlsx')

#summary of the data

data.describe()

#summary of the columns
data.info()

#counting the number of articles by source column
#format to groupby: df.grouby9=(['column_to_group'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

#number of reactions per publisher

data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column

data = data.drop('engagement_comment_plugin_count', axis = 1)

#functions in Python

def thisFunction():
    print('This is not my first function')
    
thisFunction()

this is a function with variables

def aboutme(name, lastname, location):
    print('This is '+name+' My last name is '+lastname+' I am from '+location)
    return name, lastname, location

a = aboutme('Antoinette', 'Wood', 'New Jersey')

#using for loops in functions

def favefood(food):
    for x in food:
        print('Top food is '+x)
    

fastfood = ['burgers', 'pizza', 'chicken']
favefood(fastfood)

#creating a keyword flag

keyword = 'crash'

#create a for loop to isolate each title
length = len(data)
keyword_flag = []
for x in range(0,length):
    heading = data['title'][x]
    if keyword in heading:
        flag = 1
    else:
        flag = 0
    keyword_flag.append(flag)
    


#creating a function

def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
       heading = data['title'][x]
       try:
           if keyword in heading:
              flag = 1
           else:
              flag = 0
       except:
            flag = 0
       keyword_flag.append(flag)
    return keyword_flag

keywordgflag = keywordflag('murder')

#creating a new column in data dataframe

data['keyword_flag'] = pd.Series(keywordgflag)

#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]

sent = sent_int.polarity_scores(text)    

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#writing the data

data.to_excel('BlogMe_Clean.xlsx', sheet_name = 'blogmedata', index = False)













