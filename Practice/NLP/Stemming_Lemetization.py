# Stemming And Lemmatization
import nltk
# from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')  # Downloads the WordNet corpus for lemmatization
nltk.download('omw-1.4')  # Required for lemmatization to work correctly

stemmer = nltk.PorterStemmer()

# Stemming words
words1 = ['Jumping', 'Jump', 'Jumped', 'Running', 'Runner', 'Easily']
stemmed_words = []

for word in words1:
    stemmed_words.append(stemmer.stem(word))


print("Original Words:", words1)
print("Stemmed Words:", stemmed_words)

# Lemmatization
lemmatizer = nltk.WordNetLemmatizer()

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