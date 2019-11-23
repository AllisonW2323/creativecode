#all imports
!pip install markovify
!pip install weasyprint

import markovify
from weasyprint import HTML

#end imports


novel = ''
#the text source I am using
with open("GALAXY QUEST.txt") as f:
    text = f.read()

#the markovify code that I am borrowing for this project
text_model = markovify.Text(text)


#number edited to make sure the wordcount of at least 50,000 has been reached
for i in range(5000):   
    novel += str(text_model.make_sentence()) + " "

#this next line is just so that you may see that this has an output of over 50,000 words
print(str(len(novel.split(" "))))

#this is the template for how I want the words to print on the paper
html_template = f"""
<html>
  <head>
  <title>GALAXY QUEST</title>
  </head>
  <body>
  {novel}
  </body>
</html>
"""

#this saves the sentences as a PDF using the HTML module of WeasyPrint
HTML(string=html_template).write_pdf("GALAXY QUEST_novel.pdf")
