
import numpy as np
import pandas as pd


#!pip install twitter

from twitter import Twitter
from twitter import OAuth

from pandas.io.json import json_normalize

apikey='LmWo260maj5KsmP3wnigGiymR'
apisecretkey='wdFhGB3XV79csLvSI57R1OFavsXNntbdtmlJzy2spNdMIFbnxn'
accesstoken='4012083173-pdPffs50tApeBURWR9QQt22rlhEp0sdEaCFwBvR'
accesstokensecret='PVwr62zsdUF0QQpcRMkPDBLxJ4HhAG4Cjccy49GwPv8pK'

oauth = OAuth(accesstoken,accesstokensecret,apikey,apisecretkey)
api = Twitter(auth=oauth)

tjson=api.statuses.user_timeline(screen_name="realDonaldTrump",tweet_mode='extended',count = 200)
dftrump=json_normalize(tjson)
dftrump.shape

dftrump['id']

mid = dftrump['id'].min()
mid=mid-1
tjson2=api.statuses.user_timeline(screen_name="realDonaldTrump",tweet_mode='extended',count = 200,max_id = mid)
dftrump2=json_normalize(tjson2)

mid_l=dftrump2['id'].max()

a=pd.Series([1,2,3,4,5])
b=pd.Series([10,20,30,40,50])
c=pd.Series([6,7,8,9,10])
d=pd.Series([60,70,80,90,100])

dfa=pd.DataFrame({'a':a,'b':b})
dfb=pd.DataFrame({'a':c,'b':d})
dfc=pd.concat([dfa,dfb])
dfd=pd.concat([dfa,dfb], ignore_index=True)


df = pd.DataFrame()
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
        df = pd.concat([df, dftrump], ignore_index=True)
    

df.shape




