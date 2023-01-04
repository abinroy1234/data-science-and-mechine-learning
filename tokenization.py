import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
text1 = "The data set given satisfies the requirement for model generation. This is used in Data Science Lab"
print("sentence tokenization:")
for i in sent_tokenize(text1):
 print(i)
print("word tokenization:")
for i in word_tokenize(text1):
 print(i)
text = word_tokenize(text1)
print("parts of Speech:")
for i in nltk.pos_tag(text):
 print(i)
print("after removing stop words")
text = [word for word in text if word not in stopwords.words('english')]
print(text)
# 2 grams
print("2 grams are:")

temp = zip(*[text[i:] for i in range(0, 2)])
ans = [' '.join(ngram) for ngram in temp]
print(ans)
# 4 grams
print("4 grams are:")
temp = zip(*[text[i:] for i in range(0, 4)])
ans = [' '.join(ngram) for ngram in temp]
print(ans)
