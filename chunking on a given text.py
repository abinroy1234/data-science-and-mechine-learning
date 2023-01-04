import nltk
from nltk.corpus import stopwords
sample_text="Rama Killed Ravana to save Sita from Lanka.The Legend of Ramayan is the most popular Indian epic.A lot of Movies and serials have already been shot in several languages here in india based on the ramayan."
tokenized=nltk.sent_tokenize(sample_text)
for i in tokenized:
 words=nltk.word_tokenize(i)
tagged_words=nltk.pos_tag(words)
#following statement will chunk every word in the sentence
chunkGram=r"""chunk: {<.*>+ }"""
chunkParser=nltk.RegexpParser(chunkGram)
chunked=chunkParser.parse(tagged_words)
print(chunked)
chunked.draw()
