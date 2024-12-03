import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# Example sentence
sentence = "Stemming helps in preprocessing text"

# Tokenize the sentence into words
tokens = nltk.word_tokenize(sentence)

# Perform POS tagging
tags = nltk.pos_tag(tokens)

print(tags)