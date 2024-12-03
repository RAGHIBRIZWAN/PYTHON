# Stop Words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize

nltk.download('stopwords')

text = "Hello my name is Raghib. I am 19 years old"

word = word_tokenize(text)
sent = sent_tokenize(text)

stopWords = stopwords.words('english')

filteredWords = []
filteredWords1 = []

for words in word:
    if words.lower() not in stopWords:
        filteredWords.append(words)
       
# Little bit different from the above. 
for i in range(len(sent)):
    words = word_tokenize(sent[i])
    for wording in words:
        if wording not in stopWords:
            filteredWords1.append(wording)

print(word)
print(filteredWords)
print(filteredWords1)