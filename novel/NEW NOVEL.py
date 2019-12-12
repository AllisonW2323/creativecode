from dominate.tags import *
import dominate
import markovify
from weasyprint import HTML


wc=0

novel = '<p>'
with open("movie_scripts.txt") as f:
  text = f.read()



text_model = markovify.Text(text)

# for i in range(8000): #change to 5000
#     novel += str(text_model.make_sentence()) + " "

import random


  
# a general function for making paragraphs out of sentences
def make_paragraph():
  paragraph = ""
  for i in range(random.randint(5,20)):
    paragraph += str(text_model.make_sentence()) + " "


  # wc += len(paragraph.split(" "))
  return paragraph



# initialize the HTML document
doc = dominate.document(title='Sky Quest!')

# add content to the HTML document
with doc:
  h1("Sky Quest!")
  for ch in range(10): # create 10 chapters
    h2("Commander's Log "+ str(int(ch + 1)))
    for para in range(random.randint(30,60)): #40 was 10 and 60 was 40
      p(make_paragraph())

#print(len(str(doc).split(" "))) #makes about 60,000 words!!! comment this out to stop the printing
# write the HTML document as a PDF
HTML(string=str(doc)).write_pdf("Sky Quest.pdf")
