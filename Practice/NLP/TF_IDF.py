import math
from collections import Counter

def compute_tf(term, document):
    """Calculate term frequency for a term in a document."""
    term_count = document.count(term)
    total_terms = len(document)
    return term_count / total_terms

def compute_idf(term, corpus):
    """Calculate inverse document frequency for a term."""
    num_docs_with_term = sum(1 for doc in corpus if term in doc)
    if num_docs_with_term == 0:
        return 0
    return math.log(len(corpus) / num_docs_with_term)

def compute_tfidf(corpus):
    """Calculate TF-IDF for each term in the corpus."""
    tfidf_scores = []
    for document in corpus:
        doc_scores = {}
        for term in set(document):  # Use `set` to avoid duplicate calculations
            tf = compute_tf(term, document)
            idf = compute_idf(term, corpus)
            doc_scores[term] = tf * idf
        tfidf_scores.append(doc_scores)
    return tfidf_scores

# Example usage
if __name__ == "__main__":
    # Sample corpus: List of documents (each document is a list of words)
    corpus = [
        ["the", "cat", "is", "on", "the", "mat"],
        ["dogs", "are", "in", "the", "fog"],
        ["the", "cat", "and", "the", "dog", "are", "friends"]
    ]
    
    tfidf = compute_tfidf(corpus)
    
    for i, doc_scores in enumerate(tfidf):
        print(f"Document {i + 1} TF-IDF scores:")
        for term, score in doc_scores.items():
            print(f"  {term}: {score:.4f}")