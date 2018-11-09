
# coding: utf-8

# # References : 
# 1. https://www.blog.pythonlibrary.org/2014/09/26/how-to-connect-to-twitter-with-python/
# 2. https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

# # Posting a status

# In[1]:

import tweepy
 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
client = tweepy.API(auth)
#client.update_status("Sabse Uncha Sabse Shaandaar #StatueOfUnity") # will update your twitter status
api = tweepy.API(auth, wait_on_rate_limit=True)




# ## Importing timeline

# In[2]:

timeline = client.home_timeline()
 
for item in timeline:
    text = "%s says '%s'" % (item.user.screen_name, item.text)
    print(text)


# ## Live Stream

# In[6]:

from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#StatueofUnity'])


# In[7]:

import json
 
with open('python.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=5)) # pretty-print


# ## Getting list of pages and people you follow

# In[4]:

import tweepy
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
client = tweepy.API(auth)
client = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True)

 
friends = client.friends()
     
for friend in tweepy.Cursor(client.friends).items(200):
     print(friend.name)


# ## Getting a list of followers:

# In[5]:

followers = client.followers()
for follower in followers:
    print(follower.name)
    
#for followers in tweepy.Cursor(client.followers).items(20): # prints upto 200 using tweepy cu
     #print(followers.name)


# In[ ]:



