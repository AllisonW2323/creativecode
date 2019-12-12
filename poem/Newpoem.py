import pronouncing
import random

uploaded = files.upload()
for fn in uploaded.keys():                          
  text = uploaded[fn].decode()
  
wordlist= text.split(" ")
from textblob import TextBlob

blob= TextBlob (text)

random.randint(1,6)

blob= TextBlob (text)

import nltk

nltk.download('averaged_perceptron_tagger')

import nltk
nltk.download('punkt')


bannedword=["chink", "Chink", "Niger", "niger"]   #had to write them so my bot would not




syll = random.randint(1,3)
deads = []
likes= []
loves= []


adjlist=[]
for word,tag in blob.tags:
  if tag == "JJ":
   adjlist.append(word)
    
for i in range (1):
  word1=(adjlist[random.randint(0,len(adjlist)-1)])
  word2= ( blob.words[random.randint(0,12787)])
  #poetry code borrowed from Whalen
  dead = random.choice(pronouncing.rhymes("dead"))

  for r in pronouncing.rhymes("dead"):
    rsyl = pronouncing.phones_for_word(r)
  if (pronouncing.syllable_count(rsyl[0]) is syll):
    deads.append(r)

print(dead)
#end of borrowed

if word1 not in bannedword:
  print(word1)
else:
  print("bleep")

print("                   ")
    
nounlist=[]
for word,tag in blob.tags:
  if tag == "NN":
    nounlist.append(word)
    
for i in range (1):
  word1=(nounlist[random.randint(0,len(nounlist)-1)])
  #poetry code borrowed from Whalen
  dead = random.choice(pronouncing.rhymes("dead"))

  for r in pronouncing.rhymes("dead"):
    rsyl = pronouncing.phones_for_word(r)
  if (pronouncing.syllable_count(rsyl[0]) is syll):
    deads.append(r)

print(dead)
#end of borrowed



if word1 not in bannedword:
  print(word1)
else:
  print("bleep")
    

print("                   ")
    
verblist=[]
for word,tag in blob.tags:
  if tag == "VB":
    verblist.append(word)
    
for i in range (1):
  word1=(verblist[random.randint(0,len(verblist)-1)])
  print( blob.words[random.randint(0,12787)])
  #poetry code borrowed from Whalen
  like = random.choice(pronouncing.rhymes("like"))

  for r in pronouncing.rhymes("like"):
    rsyl = pronouncing.phones_for_word(r)
  if (pronouncing.syllable_count(rsyl[0]) is syll):
    likes.append(r)

print(like)
#end of borrowed

if word1 not in bannedword:
  print(word1)
else:
  print("bleep")
    

print("                   ")

for i in range(1):
    print (blob.sentences[random.randint (0,len(blob.sentences))])
    #poetry code borrowed from whalen
    like = random.choice(pronouncing.rhymes("like"))

for r in pronouncing.rhymes("like"):
  rsyl = pronouncing.phones_for_word(r)
if (pronouncing.syllable_count(rsyl[0]) is syll):
  likes.append(r)

print(like)
#end of borrowed

verblist=[]
for word,tag in blob.tags:
  if tag == "VB":
    verblist.append(word)
    
for i in range (1):
  word1=(verblist[random.randint(0,len(verblist)-1)])
  print( blob.words[random.randint(0,12787)])
  #poetry code borrowed from Whalen
  love = random.choice(pronouncing.rhymes("love"))

for r in pronouncing.rhymes("love"):
  rsyl = pronouncing.phones_for_word(r)
if (pronouncing.syllable_count(rsyl[0]) is syll):
  loves.append(r)

print(love)
#end of borrowed

if word1 not in bannedword:
  print(word1)
else:
  print("bleep")

print("                   ")

for i in range(1):
    print (blob.sentences[random.randint (0,len(blob.sentences))])
    
  
nounlist=[]
for word,tag in blob.tags:
  if tag == "NN":
    nounlist.append(word)


for i in range (1):
  word1=(nounlist[random.randint(0,len(nounlist)-1)])
  
#poetry code borrowed from Whalen
  love = random.choice(pronouncing.rhymes("love"))

for r in pronouncing.rhymes("love"):
  rsyl = pronouncing.phones_for_word(r)
if (pronouncing.syllable_count(rsyl[0]) is syll):
  loves.append(r)

print(love)
#end of borrowed

if word1 not in bannedword:
  print(word1)
else:
  print("bleep")


