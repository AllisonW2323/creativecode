from google.colab import files
import random

uploaded = files.upload()
for fn in uploaded.keys():
  text = uploaded[fn].decode()
  
wordlist= text.split(" ")
from textblob import TextBlob

blob= TextBlob (text)

random.randint(1,6)
!pip install textblob
from textblob import TextBlob

blob= TextBlob (text)

import nltk

nltk.download('averaged_perceptron_tagger')

import nltk
nltk.download('punkt')


Bannedword=["chink", "Chink", "Niger", "niger"]   #had to write them so my bot would not



adjlist=[]
for word,tag in blob.tags:
  if tag == "JJ":
   adjlist.append(word)
    
for i in range (1):
  word1=(adjlist[random.randint(0,len(adjlist)-1)])
  if word1 not in Bannedword:
    print(word1)
  else:
    print("bleep")
    
    
nounlist=[]
for word,tag in blob.tags:
  if tag == "NN":
    nounlist.append(word)
    
for i in range (1):
  word1=(nounlist[random.randint(0,len(nounlist)-1)])
  if word1 not in Bannedword:
    print(word1)
  else:
    print("bleep")
    
    
verblist=[]
for word,tag in blob.tags:
  if tag == "VB":
    verblist.append(word)
    
for i in range (1):
  word1=(verblist[random.randint(0,len(verblist)-1)])
  if word1 not in Bannedword:
    print(word1)
  else:
    print("bleep")

for i in range(1):
    print (blob.sentences[random.randint (0,len(blob.sentences))])
    
verblist=[]
for word,tag in blob.tags:
  if tag == "VB":
    verblist.append(word)
    
for i in range (1):
  word1=(verblist[random.randint(0,len(verblist)-1)])
  if word1 not in Bannedword:
    print(word1)
  else:
    print("bleep")
  
nounlist=[]
for word,tag in blob.tags:
  if tag == "NN":
    nounlist.append(word)
    
for i in range (1):
  #print(nounlist[random.randint(0,len(nounlist)-1)]) 
  word1=(nounlist[random.randint(0,len(nounlist)-1)])
  if word1 not in Bannedword:
    print(word1)
  else:
    print("bleep")
