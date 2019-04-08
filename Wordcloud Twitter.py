
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

#####  new imports ##################
import pip

#!pip install wordcloud

from nltk.corpus import stopwords

import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop =stopwords.words('english')

wordcloud = WordCloud().generate(df.full_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud2 = WordCloud(background_color="white",stopwords=stop).generate(tx)
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()

# Display the generated image:
tx2=df.full_text.str.cat(sep=' ')

wordcloud3 = WordCloud(stopwords=stop).generate(tx2)
plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis("off")
plt.show()

stop.append('RT')
stop.append('co')
stop.append('https')
stop.append('amp')

wordcloud4 = WordCloud(background_color="white",stopwords=stop,max_words=1000).generate(tx2)
plt.imshow(wordcloud4, interpolation='bilinear')
plt.axis("off")
plt.show()



