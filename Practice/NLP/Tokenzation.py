# Tokenization
import nltk
nltk.download('punkt_tab') # Mandatory to download for tokenization

# from nltk.tokenize import word_tokenize,sent_tokenize

text = "Hello my name is Raghib. I am 19 years old"

word = nltk.word_tokenize(text)
print(word)

sent = nltk.sent_tokenize(text)
print(sent)