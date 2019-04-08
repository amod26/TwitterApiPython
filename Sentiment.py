#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:56:02 2019

@author: wajgilani
"""

import numpy as np
import pandas as pd


#!pip install twitter

from twitter import Twitter
from twitter import OAuth

from pandas.io.json import json_normalize

from textblob import TextBlob
from nltk.corpus import stopwords
stop =stopwords.words('english')


apikey='LmWo260maj5KsmP3wnigGiymR'
apisecretkey='wdFhGB3XV79csLvSI57R1OFavsXNntbdtmlJzy2spNdMIFbnxn'
accesstoken='4012083173-pdPffs50tApeBURWR9QQt22rlhEp0sdEaCFwBvR'
accesstokensecret='PVwr62zsdUF0QQpcRMkPDBLxJ4HhAG4Cjccy49GwPv8pK'

oauth = OAuth(accesstoken,accesstokensecret,apikey,apisecretkey)
api = Twitter(auth=oauth)

dflab5 = pd.DataFrame()
mid=0
for i in range(34):
    if i==0:
        tjson=api.statuses.user_timeline(screen_name="realDonaldTrump",tweet_mode='extended',count = 200)
    else:
        tjson=api.statuses.user_timeline(screen_name="realDonaldTrump",tweet_mode='extended',count = 200,max_id = mid)
    if len(tjson)>0:
        dftrump=json_normalize(tjson)
        mid=dftrump['id'].min()
        mid=mid-1
        #df = df.append(df,ignore_index=True)
        dflab5 = pd.concat([dflab5, dftrump], ignore_index=True)
        
#dflab5.to_pickle('dflab5.pkl')
dflab5=pd.read_pickle('dflab5.pkl')
        
df=dflab5[['created_at','full_text']]

polarity=[]
subj=[]

#Get polarity and sentiment for each row and put it in either polarity or sentiment 
for t in df.full_text:
    tx=TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    subj.append(tx.sentiment.subjectivity)

df.loc[:,'polarity']=polarity
df['subj']=subj

df['lft']=df.full_text.str.lower()
df['ft_list']=df.lft.str.split()
df['ft_array']=df.ft_list.apply(np.array)

type(df.loc[0,'ft_array'])

aaa=np.array(['hi','buy','i','i','waj','apple','bananna'])
aaa[~np.isin(aaa,stop)]

df.loc[0,'ft_array'][~np.isin(df.loc[0,'ft_array'],stop)]

df.loc[:,'ft_a_stop']=df.ft_array.apply(lambda x: x[~np.isin(x,stop)])


df.loc[:,'pd_ft']=df.ft_a_stop.apply(lambda x: pd.Series(x)[~pd.Series(x).str.contains('http')].values)
    

df.loc[:,'pd_ft2']=df.pd_ft.apply(lambda x: pd.Series(x)[~pd.Series(x).str.contains('rt')].values)

df.loc[:,'pd_ft3']=df.pd_ft2.apply(lambda x: pd.Series(x)[~pd.Series(x).str.contains('@')].values)


df.loc[:,'ft_clean']=df.pd_ft3.apply(lambda x: ' '.join(x))

df.loc[:,'ft_clean_l']=df.pd_ft3.apply(lambda x: x.tolist())

ft_list_l=[]
df.ft_list.apply(lambda x: ft_list_l.extend(x))


dfwords=pd.DataFrame({'w':ft_list_l,'w2':ft_list_l})
dfw=dfwords.groupby('w')['w2'].count().reset_index()
dfw.sort_values('w2',ascending=False,inplace=True)
dfw.head(30).plot.bar(x='w',y='w2')

dfw['perc']= dfw['w2']/dfw['w2'].sum()

np.random.choice(dfw.w.tolist(), 3, dfw.perc.tolist())

ft_list_cl=[]
df.ft_clean_l.apply(lambda x: ft_list_cl.extend(x))


dfwords2=pd.DataFrame({'w':ft_list_cl,'w2':ft_list_cl})
dfw2=dfwords2.groupby('w')['w2'].count().reset_index()
dfw2.sort_values('w2',ascending=False,inplace=True)
dfw2.head(30).plot.bar(x='w',y='w2')

dfw2['perc']= dfw2['w2']/dfw2['w2'].sum()

np.random.choice(dfw2.w.tolist(), 10, dfw2.perc.tolist())