# Tokenization

import nltk
nltk.download('punkt_tab') # Mandatory to download for tokenization

from nltk.tokenize import word_tokenize,sent_tokenize

text = "Hello my name is Raghib. I am 19 years old"

word = word_tokenize(text)
print(word)

sent = sent_tokenize(text)
print(sent)

# Stemming And Lemmatization
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')  # Downloads the WordNet corpus for lemmatization
nltk.download('omw-1.4')  # Required for lemmatization to work correctly

stemmer = PorterStemmer()

# Stemming words
words1 = ['Jumping', 'Jump', 'Jumped', 'Running', 'Runner', 'Easily']
stemmed_words = []

for word in words1:
    stemmed_word = stemmer.stem(word)
    stemmed_words.append(stemmed_word)


print("Original Words:", words1)
print("Stemmed Words:", stemmed_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()

words2 = ['Jumping', 'Jump', 'Jumps', 'Running', 'Runner', 'Easily']

lemmatized_noun = []
lemmatized_verb = []

for word in words2:
    lemmatized_noun.append(lemmatizer.lemmatize(word, pos='n'))

for word in words2:
    lemmatized_verb.append(lemmatizer.lemmatize(word, pos='v'))

print("Original Words:", words2)
print("Lemmatized as Noun:", lemmatized_noun)
print("Lemmatized as Verb:", lemmatized_verb)

# Stop Words

from nltk.corpus import stopwords

nltk.download('stopwords')

stopWords = set(stopwords.words('english'))

filteredWords = []

for words in word:
    if words.lower() not in stopWords:
        filteredWords.append(words)

print(word)
print(filteredWords)

para = '''
Pakistan, officially known as the Islamic Republic of Pakistan, is a country 
in South Asia, bordered by India to the east, Afghanistan and Iran to the west, and China to the north. 
It has a diverse geography, ranging from the towering peaks of the Himalayas and the Karakoram in the north to the fertile plains of 
the Punjab and Sindh and the arid deserts of Balochistan. With a population of over 230 million, Pakistan is the world's fifth-most 
populous country and has a rich cultural heritage influenced by numerous 
civilizations, including the Indus Valley Civilization, one of the oldest in the world. Pakistan’s official language is Urdu, 
though many regional languages are spoken across its provinces. Islamabad, the capital, is known for its modern architecture and scenic 
beauty, while Karachi and Lahore are vibrant cities with significant historical and economic importance.
'''

sentences = sent_tokenize(para)
stop_words = set(stopwords.words('english'))

for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    filtered_words = []
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(stemmer.stem(word))
    sentences[i] = ' '.join(filtered_words)

print(sentences)