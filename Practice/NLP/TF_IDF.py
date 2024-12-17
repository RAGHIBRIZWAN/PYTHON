import nltk
from nltk.corpus import stopwords

para = 'Pakistan was established in 1947'

wordnet = nltk.WordNetLemmatizer()
sentences = nltk.sent_tokenize()

review = []
corpus = []
for word in sentences:
    if word not in set(stopwords.words('english')):
        review.append(wordnet.lemmatize(word))
        
    review = ' '.join(review)
    corpus.append(review)
    
# Creating bag of models
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()

# For Tf-Idf
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer()
x = cv.fit_transform(corpus).toarray()
